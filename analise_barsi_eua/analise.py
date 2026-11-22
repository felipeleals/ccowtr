"""Retorno de 10 anos (preço + dividendos reinvestidos) de ações americanas em setores 'Barsi'.
Fonte: Yahoo Finance chart API (preço diário ajustado por splits; adjclose = dividendos reinvestidos)."""
import json, time, urllib.request, sys
import pandas as pd

SETORES = {
 "Bancos": "JPM BAC WFC C USB PNC TFC MTB FITB GS MS BK".split(),
 "Energia elétrica": "DUK NEE SO D AEP XEL ED WEC EXC SRE ETR PEG CMS DTE AEE ATO NI PPL CNP EIX FE ES LNT EVRG".split(),
 "Saneamento": "AWK AWR CWT WTRG MSEX YORW HTO".split(),
 "Seguros": "CB TRV ALL PGR AIG MET PRU AFL HIG CINF WRB MRSH AJG AON RLI".split(),
 "Telecom": "VZ T TMUS CMCSA".split(),
}
CITADOS = "JPM BAC DUK NEE SO AWK CB TRV".split()
ANOS = 10

import os
CACHE = "analise_barsi_eua/cache"
os.makedirs(CACHE, exist_ok=True)

def baixar(t):
    f = f"{CACHE}/{t}.json"
    if os.path.exists(f):
        return json.load(open(f))
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?period1=1447000000&period2={int(time.time())}&interval=1d&events=div%7Csplit"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    for i in range(6):
        try:
            r = json.load(urllib.request.urlopen(req, timeout=30))["chart"]["result"][0]
            if "timestamp" in r:
                json.dump(r, open(f, "w"))
                return r
        except Exception as e:
            print("retry", t, e, file=sys.stderr)
        time.sleep(3 * (i + 1))
    return {}

linhas = []
for setor, tks in SETORES.items():
    for t in tks:
        r = baixar(t)
        if "timestamp" not in r:
            print("sem dados:", t, file=sys.stderr); continue
        idx = pd.to_datetime(r["timestamp"], unit="s").normalize()
        q = r["indicators"]["quote"][0]
        df = pd.DataFrame({"close": q["close"], "adj": r["indicators"]["adjclose"][0]["adjclose"]}, index=idx).dropna()
        divs = pd.Series({pd.to_datetime(int(k), unit="s"): v["amount"] for k, v in r.get("events", {}).get("dividends", {}).items()}, dtype=float).sort_index()
        fim = df.index[-1]
        ini_alvo = fim - pd.DateOffset(years=ANOS)
        df10 = df[df.index >= ini_alvo]
        if df10.index[0] - ini_alvo > pd.Timedelta(days=10):
            print("histórico curto:", t, file=sys.stderr); continue
        p0, p1 = df10["close"].iloc[0], df10["close"].iloc[-1]
        a0, a1 = df10["adj"].iloc[0], df10["adj"].iloc[-1]
        anos = (df10.index[-1] - df10.index[0]).days / 365.25
        ttm = divs[divs.index > fim - pd.DateOffset(years=1)].sum()
        ttm0 = divs[(divs.index > ini_alvo - pd.DateOffset(years=1)) & (divs.index <= ini_alvo)].sum()
        dps_cagr = (ttm / ttm0) ** (1 / anos) - 1 if ttm0 > 0 and ttm > 0 else float("nan")
        linhas.append(dict(
            ticker=t, setor=setor,
            preco_ini=round(p0, 2), preco_atual=round(p1, 2),
            ret_preco_pct=round((p1 / p0 - 1) * 100, 1),
            ret_total_pct=round((a1 / a0 - 1) * 100, 1),
            cagr_preco_pct=round(((p1 / p0) ** (1 / anos) - 1) * 100, 2),
            cagr_total_pct=round(((a1 / a0) ** (1 / anos) - 1) * 100, 2),
            div_12m_ini=round(ttm0, 2), div_12m_atual=round(ttm, 2),
            cagr_dividendo_pct=round(dps_cagr * 100, 2),
            yield_atual_pct=round(ttm / p1 * 100, 2),
            yield_sobre_custo_pct=round(ttm / p0 * 100, 2),
            mil_viraram=round(1000 * a1 / a0),
            data_ini=df10.index[0].date(), data_fim=fim.date(),
        ))
        time.sleep(1)

res = pd.DataFrame(linhas).sort_values("ret_total_pct", ascending=False).reset_index(drop=True)
res.index += 1
res.to_csv("analise_barsi_eua/universo_completo.csv", index_label="rank")
pd.set_option("display.width", 250); pd.set_option("display.max_columns", 30)
print(res.to_string())
