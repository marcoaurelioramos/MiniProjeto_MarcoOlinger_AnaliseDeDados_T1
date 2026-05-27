import pandas as pd
import numpy as np

df_varejo = pd.read_csv('D:\\SCTEC\\Base Varejo.csv',sep=';')

print(df_varejo.head())
print(df_varejo.shape)
print(df_varejo.info())

# Verificação de Inconsistências Iniciais 
print("Valores nulos por coluna:")
print(df_varejo.isnull().sum())
print(f"\nQuantidade de linhas duplicadas: {df_varejo.duplicated().sum()}")

# Verifiquei que foram importadas colunas em branco, farei a remoção delas.
df_varejo = df_varejo.drop(['Unnamed: 10', 'Unnamed: 11','Unnamed: 12','Unnamed: 13'], axis=1)
print(df_varejo.info())


# Remoção espaços em branco extras na coluna PR_CAT
if 'PR_CAT' in df_varejo.columns:
    df_varejo['PR_CAT'] = df_varejo['PR_CAT'].astype(str).str.strip().str.capitalize()
print(df_varejo)


#Conversão da coluna Data de String para Date/Time
df_varejo['DATA_CONVERTIDA'] = pd.to_datetime(df_varejo['DATA'], format='%d/%m/%Y', errors='coerce')                                          
print(df_varejo.info())
print(df_varejo.head)