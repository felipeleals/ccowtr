"""Gera séries para os gráficos: índice mensal de preço e retorno total (base 100) e dividendos anuais."""
import json, pandas as pd
res = pd.read_csv("analise_barsi_eua/universo_completo.csv")
tks = list(res.head(12).ticker) + [t for t in "CB SO BAC DUK AWK".split() if t not in list(res.head(12).ticker)]
ev, dv = [], []
for t in tks:
    r = json.load(open(f"analise_barsi_eua/cache/{t}.json"))
    idx = pd.to_datetime(r["timestamp"], unit="s").normalize()
    df = pd.DataFrame({"close": r["indicators"]["quote"][0]["close"], "adj": r["indicators"]["adjclose"][0]["adjclose"]}, index=idx).dropna()
    df = df[df.index >= pd.Timestamp(res.loc[res.ticker == t, "data_ini"].iloc[0])]
    m = df.resample("ME").last(); m.iloc[0] = df.iloc[0]
    m = pd.concat([df.iloc[[0]], df.resample("ME").last().iloc[:-1], df.iloc[[-1]]])
    for d, row in m.iterrows():
        ev.append(dict(data=d.strftime("%Y-%m-%d"), ticker=t, preco=round(row.close / df.close.iloc[0] * 100, 1), total=round(row.adj / df.adj.iloc[0] * 100, 1)))
    s = pd.Series({pd.to_datetime(int(k), unit="s"): v["amount"] for k, v in r["events"]["dividends"].items()})
    a = s.groupby(s.index.year).sum()
    for y in range(2016, 2026):
        dv.append(dict(ano=y, ticker=t, dividendo=round(float(a.get(y, 0)), 2)))
pd.DataFrame(ev).to_csv("analise_barsi_eua/evolucao_mensal.csv", index=False)
pd.DataFrame(dv).to_csv("analise_barsi_eua/dividendos_anuais.csv", index=False)
print(len(ev), len(dv), tks)

# Yield sem dividendos extraordinários: um pagamento acima de 3x a mediana dos 8 últimos conta só como a mediana (parte regular).
ys = []
for t in res.ticker:
    r = json.load(open(f"analise_barsi_eua/cache/{t}.json"))
    s = pd.Series({pd.to_datetime(int(k), unit="s"): v["amount"] for k, v in r.get("events", {}).get("dividends", {}).items()}, dtype=float).sort_index()
    fim = pd.Timestamp(res.loc[res.ticker == t, "data_fim"].iloc[0])
    u = s[s.index > fim - pd.DateOffset(years=1)]
    med = s.iloc[-8:].median() if len(s) else 0
    reg = u.where(u <= 3 * med, med).sum() if len(u) else 0.0
    ys.append(round(reg / res.loc[res.ticker == t, "preco_atual"].iloc[0] * 100, 2))
res["yield_sem_extra_pct"] = ys
res.to_csv("analise_barsi_eua/universo_completo.csv", index=False)
print(res.loc[res.yield_sem_extra_pct != res.yield_atual_pct, ["ticker", "yield_atual_pct", "yield_sem_extra_pct"]])
