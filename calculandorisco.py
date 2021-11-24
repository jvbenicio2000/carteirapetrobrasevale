import pandas as pd
import numpy as np
# fim das bibliotecas
wb=pd.read_excel("planilhavolatilidade.xlsx")
df=pd.DataFrame(wb)
df = df[['petr', 'valor', 'vale', 'valor.1', 'usdbrl', 'valor.2', 'di','valor.3']]
# print(df.columns)
# print(df.head())
equity=df[["petr","valor","vale","valor.1"]]

eq=equity.rename(columns={"petr":"data","valor":"petr","vale":"data2","valor.1":"vale"})
equity=eq[["data","petr","vale"]]

# Calculando o retorno percentual analisado
equity["var_per_vale_anu"] = (equity["vale"].pct_change())
equity["var_per_petr_anu"] = (equity["petr"].pct_change())
# print(equity.head(5))
equity["di_diario"]=((df["valor.3"]+1)**(1/252))-1
# print(equity.head())
ex_returns = equity
ex_returns["retorno_e_vale"]=equity["var_per_vale_anu"]-equity["di_diario"]
ex_returns["retorno_e_petr"]=equity["var_per_petr_anu"]-equity["di_diario"]
ex_returns=ex_returns[["retorno_e_vale","retorno_e_petr"]]
# print(ex_returns[0])
carteira={"vale":0.4,"petr":0.4,"di_diario":0.2}
total=10000
carteira_valores=pd.DataFrame()
petr4_valor_inv=total*carteira["petr"]
valor_inicial_petr=list(equity["petr"])[0]
# print(valor_inicial_petr)
numero_petr4=petr4_valor_inv/valor_inicial_petr
print(numero_petr4)