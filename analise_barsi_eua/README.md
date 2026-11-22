# 10 anos de ações americanas no estilo Barsi

Período: **21/11/2016 a 20/11/2026**. Fonte: Yahoo Finance (preço diário ajustado por desdobramentos; o retorno total usa o preço ajustado com dividendos reinvestidos, sem impostos).
Universo: 61 empresas de bancos, energia elétrica, saneamento, seguros e telecom. A BK (BNY) ficou de fora porque a Yahoo não devolveu dados. Arquivo completo: [`universo_completo.csv`](universo_completo.csv). Script: [`analise.py`](analise.py).

Para comparar: o S&P 500 com dividendos rendeu cerca de 13 a 14% ao ano no período (referência aproximada, não calculada aqui).

## As 12 que mais renderam (retorno total)

| # | Ticker | Setor | Retorno total 10a | CAGR total | Retorno só preço | CAGR preço | US$1.000 viraram | Div. 12m (2016 → 2026) | CAGR dividendo | Yield atual | Yield s/ custo |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **PGR** | Seguros | 828% | 25.0% | 602% | 21.5% | 9,277 | 0.89 → 13.90 | 31.7% | 6.0% | 42.2% |
| 2 | **AJG** | Seguros | 535% | 20.3% | 443% | 18.4% | 6,349 | 1.51 → 2.75 | 6.2% | 1.0% | 5.3% |
| 3 | **MS** | Bancos | 441% | 18.4% | 308% | 15.1% | 5,412 | 0.70 → 4.30 | 19.9% | 2.6% | 10.6% |
| 4 | **WRB** | Seguros | 440% | 18.4% | 335% | 15.8% | 5,396 | 0.44 → 1.88 | 15.5% | 2.4% | 10.4% |
| 5 | **JPM** | Bancos | 416% | 17.9% | 298% | 14.8% | 5,163 | 1.84 → 6.15 | 12.8% | 2.0% | 7.9% |
| 6 | **ALL** | Seguros | 361% | 16.5% | 270% | 14.0% | 4,608 | 1.29 → 4.24 | 12.6% | 1.6% | 5.9% |
| 7 | **GS** | Bancos | 361% | 16.5% | 275% | 14.1% | 4,607 | 2.60 → 18.00 | 21.4% | 2.3% | 8.5% |
| 8 | **ETR** | Energia elétrica | 341% | 16.0% | 205% | 11.8% | 4,414 | 1.71 → 2.60 | 4.3% | 2.5% | 7.6% |
| 9 | **AFL** | Seguros | 337% | 15.9% | 247% | 13.3% | 4,369 | 0.83 → 2.44 | 11.4% | 2.0% | 6.8% |
| 10 | **TRV** | Seguros | 335% | 15.8% | 252% | 13.4% | 4,352 | 2.56 → 4.70 | 6.3% | 1.2% | 4.2% |
| 11 | **NEE** | Energia elétrica | 277% | 14.2% | 192% | 11.3% | 3,769 | 0.85 → 2.44 | 11.2% | 2.9% | 8.5% |
| 12 | **HIG** | Seguros | 258% | 13.6% | 189% | 11.2% | 3,580 | 0.84 → 2.40 | 11.1% | 1.8% | 5.1% |

## As 8 já citadas

| # | Ticker | Setor | Retorno total 10a | CAGR total | Retorno só preço | CAGR preço | US$1.000 viraram | Div. 12m (2016 → 2026) | CAGR dividendo | Yield atual | Yield s/ custo |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 5 | **JPM** | Bancos | 416% | 17.9% | 298% | 14.8% | 5,163 | 1.84 → 6.15 | 12.8% | 2.0% | 7.9% |
| 10 | **TRV** | Seguros | 335% | 15.8% | 252% | 13.4% | 4,352 | 2.56 → 4.70 | 6.3% | 1.2% | 4.2% |
| 11 | **NEE** | Energia elétrica | 277% | 14.2% | 192% | 11.3% | 3,769 | 0.85 → 2.44 | 11.2% | 2.9% | 8.5% |
| 14 | **CB** | Seguros | 247% | 13.3% | 192% | 11.3% | 3,474 | 2.72 → 3.01 | 1.0% | 0.8% | 2.4% |
| 21 | **SO** | Energia elétrica | 194% | 11.4% | 96% | 7.0% | 2,945 | 2.22 → 3.02 | 3.1% | 3.2% | 6.3% |
| 23 | **BAC** | Bancos | 189% | 11.2% | 131% | 8.8% | 2,893 | 0.23 → 1.16 | 17.8% | 2.5% | 5.7% |
| 33 | **DUK** | Energia elétrica | 161% | 10.1% | 74% | 5.7% | 2,609 | 3.36 → 4.30 | 2.5% | 3.3% | 5.8% |
| 35 | **AWK** | Saneamento | 152% | 9.7% | 106% | 7.5% | 2,519 | 1.46 → 3.51 | 9.1% | 2.4% | 4.8% |

## Por setor

| Setor | Empresas | CAGR total mediano | CAGR dividendo mediano | Yield atual mediano | Melhor do setor |
|---|---|---|---|---|---|
| Seguros | 15 | 13.4% | 6.7% | 2.0% | PGR |
| Bancos | 11 | 10.4% | 12.8% | 2.6% | MS |
| Energia elétrica | 24 | 9.9% | 5.7% | 3.2% | ETR |
| Saneamento | 7 | 5.6% | 6.8% | 2.7% | AWK |
| Telecom | 4 | 4.9% | 2.2% | 5.1% | TMUS |

## Como ler

- **Retorno total**: preço mais dividendos reinvestidos. **CAGR**: taxa média anual composta.
- **Div. 12m**: dividendos pagos por ação nos 12 meses até cada ponta do período. **CAGR dividendo**: crescimento anual dessa renda.
- **Yield s/ custo**: dividendo atual dividido pelo preço de 10 anos atrás, ou seja, quanto rende hoje quem comprou lá.
- **PGR e RLI pagam dividendos extraordinários.** O yield de 6% da PGR é distorcido por um dividendo especial de US$13,60 pago em jan/2026, já que o dividendo regular é de apenas US$0,10 por trimestre. Não conte com isso como renda fixa.
- **TMUS** só começou a pagar dividendos em 2023, por isso não tem CAGR de dividendo.

## Conclusões

1. **Seguros e bancos de investimento dominaram.** Das 12 primeiras, 7 são seguradoras ou corretoras de seguros (PGR, AJG, WRB, ALL, AFL, TRV, HIG), 3 são bancos (MS, JPM, GS) e 2 são elétricas (ETR, NEE).
2. **Elétricas entregam o que Barsi promete: renda estável, mas retorno total menor.** O CAGR mediano fica perto de 10% ao ano, com yield de cerca de 3% e dividendo crescendo 5 a 6% ao ano.
3. **Saneamento decepcionou no período.** O melhor do setor foi a AWK, com 9,7% ao ano, e o yield do setor fica perto de 2,5%.
4. **Telecom destruiu valor em preço.** VZ e T valem menos hoje que em 2016, e a T cortou o dividendo. Yield alto sem crescimento é armadilha, e a TMUS (crescimento, quase sem dividendo) foi a única boa do setor.
5. **O tradeoff de sempre:** as que mais renderam hoje pagam yield baixo (AJG 1,0%, TRV 1,2%, CB 0,8%). Quem quer renda imediata acaba nas elétricas e nos bancos regionais (yield de 3 a 4,5%) e abre mão de crescimento.

*Análise de referência, não recomendação de investimento. Rentabilidade passada não garante rentabilidade futura. Não considera a retenção de 30% de IR sobre dividendos pagos a não residentes nem o câmbio.*
