#EXTRAÇÃO E VALIDAÇÃO

import pandas as pd
df = pd.read_csv("ocorrencia.csv", parse_dates=['ocorrencia_dia'])
df.head(10)
df.dtypes
df.ocorrencia_dia.dt.month