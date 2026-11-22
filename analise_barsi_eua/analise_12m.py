"""Últimos 12 meses: retorno total e de preço, dividendos e yield das mesmas 60 empresas (usa o cache de analise.py)."""
import json, pandas as pd
base = pd.read_csv("analise_barsi_eua/universo_completo.csv")
linhas, ev, dv = [], [], []
for _, b in base.iterrows():
    t = b.ticker
    r = json.load(open(f"analise_barsi_eua/cache/{t}.json"))
    idx = pd.to_datetime(r["timestamp"], unit="s").normalize()
    df = pd.DataFrame({"close": r["indicators"]["quote"][0]["close"], "adj": r["indicators"]["adjclose"][0]["adjclose"]}, index=idx).dropna()
    fim = df.index[-1]; ini = fim - pd.DateOffset(years=1)
    d = df[df.index >= ini]
    s = pd.Series({pd.to_datetime(int(k), unit="s"): v["amount"] for k, v in r.get("events", {}).get("dividends", {}).items()}, dtype=float).sort_index()
    u = s[s.index > ini]; prev = s[(s.index > ini - pd.DateOffset(years=1)) & (s.index <= ini)]
    med = s.iloc[-8:].median() if len(s) else 0
    reg = u.clip(upper=3 * med).where(u <= 3 * med, med).sum(); regp = prev.where(prev <= 3 * med, med).sum()
    p0, p1, a0, a1 = d.close.iloc[0], d.close.iloc[-1], d.adj.iloc[0], d.adj.iloc[-1]
    dd = (d.adj / d.adj.cummax() - 1).min()
    linhas.append(dict(ticker=t, setor=b.setor, preco_ini=round(p0, 2), preco_atual=round(p1, 2),
        ret_total_pct=round((a1 / a0 - 1) * 100, 1), ret_preco_pct=round((p1 / p0 - 1) * 100, 1),
        queda_max_pct=round(dd * 100, 1),
        div_12m=round(reg, 2), div_12m_anterior=round(regp, 2),
        cresc_dividendo_pct=round((reg / regp - 1) * 100, 1) if regp > 0 else None,
        yield_atual_pct=round(reg / p1 * 100, 2), extra_12m=round(u.sum() - reg, 2),
        cagr_total_10a_pct=b.cagr_total_pct, rank_10a=b["rank"],
        data_ini=d.index[0].date(), data_fim=fim.date()))
res = pd.DataFrame(linhas).sort_values("ret_total_pct", ascending=False).reset_index(drop=True)
res.insert(0, "rank", res.index + 1)
res.to_csv("analise_barsi_eua/ranking_12m.csv", index=False)
top = res.head(12)
for _, b in top.iterrows():
    t = b.ticker
    r = json.load(open(f"analise_barsi_eua/cache/{t}.json"))
    idx = pd.to_datetime(r["timestamp"], unit="s").normalize()
    df = pd.DataFrame({"close": r["indicators"]["quote"][0]["close"], "adj": r["indicators"]["adjclose"][0]["adjclose"]}, index=idx).dropna()
    d = df[df.index >= pd.Timestamp(b.data_ini)]
    for dt, x in d.iterrows():
        ev.append(dict(data=dt.strftime("%Y-%m-%d"), ticker=t, preco=round(x.close / d.close.iloc[0] * 100, 1), total=round(x.adj / d.adj.iloc[0] * 100, 1)))
    s = pd.Series({pd.to_datetime(int(k), unit="s"): v["amount"] for k, v in r.get("events", {}).get("dividends", {}).items()}, dtype=float).sort_index()
    fim = pd.Timestamp(b.data_fim)
    for dt, v in s[s.index > fim - pd.DateOffset(years=2)].items():
        dv.append(dict(data=dt.strftime("%Y-%m-%d"), ticker=t, dividendo=round(v, 4), periodo="Últimos 12 meses" if dt > fim - pd.DateOffset(years=1) else "12 meses anteriores"))
pd.DataFrame(ev).to_csv("analise_barsi_eua/evolucao_12m.csv", index=False)
pd.DataFrame(dv).to_csv("analise_barsi_eua/dividendos_24m.csv", index=False)
pd.set_option("display.width", 250); pd.set_option("display.max_columns", 30)
print(res.head(15).to_string(index=False)); print(res[["ret_total_pct"]].describe().T)
print(res.groupby("setor").ret_total_pct.median())
