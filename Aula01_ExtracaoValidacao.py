#EXTRAÇÃO E VALIDAÇÃO

import pandas as pd
import pandera as pd (pip install pandera --user)
df = pd.read_csv("ocorrencia.csv", parse_dates=['ocorrencia_dia'], dayfirst=True)
df.head(10)
df.dtypes
df.ocorrencia_dia.dt.month
