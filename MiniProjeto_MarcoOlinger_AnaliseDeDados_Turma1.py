import pandas as pd
import numpy as np

df_varejo = pd.read_csv('D:\\SCTEC\\Base Varejo.csv',sep=';')

print(df_varejo.head())
print(df_varejo.shape)
print(df_varejo.info())