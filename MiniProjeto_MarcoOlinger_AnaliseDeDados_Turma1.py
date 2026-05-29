# Mini Projeto de Análise de Dados - Marco Olinger
# Turma 1 - Análise de Dados

#Importação das bibliotecas necessárias
import pandas as pd
import numpy as np

# Carregamento da base de dados
df_varejo = pd.read_csv('D:\\SCTEC\\Base Varejo.csv',sep=';')

print(df_varejo.head())
print(df_varejo.shape)
print(df_varejo.info())
print()
print('################################################################################')


# Verificação de Inconsistências Iniciais 
print("Valores nulos por coluna:")
print(df_varejo.isnull().sum())
print(f"\nQuantidade de linhas duplicadas: {df_varejo.duplicated().sum()}")
print()
print('################################################################################')


# Verifiquei que foram importadas colunas em branco, farei a remoção delas.
df_varejo_limpo = df_varejo.drop(['Unnamed: 10', 'Unnamed: 11','Unnamed: 12','Unnamed: 13'], axis=1)
print(df_varejo_limpo.info())


print()
print('################################################################################')
# Remoção espaços em branco extras na coluna PR_CAT
if 'PR_CAT' in df_varejo_limpo.columns:
    df_varejo_limpo['PR_CAT'] = df_varejo_limpo['PR_CAT'].astype(str).str.strip().str.capitalize()
print(df_varejo_limpo)


print()
print('################################################################################')
#Conversão da coluna Data de String para Date/Time
df_varejo_limpo['DATA_CONVERTIDA'] = pd.to_datetime(df_varejo_limpo['DATA'], format='%d/%m/%Y', errors='coerce')                                          

print(df_varejo_limpo.info())
print(df_varejo_limpo.head)


print()
print('################################################################################')
# Verificação de linhas com campos  vazios
# 1. Transformar espaço em branco em NaN real
df_varejo_limpo_analise = df_varejo_limpo.replace(r'^\s*$', np.nan, regex=True)

# 2. Exibir o total real de campos vazios por coluna
print("Total de vazios por coluna:")
print(df_varejo_limpo_analise.isna().sum())


print()
print('################################################################################')
# Remoção de linhas duplicadas
print(f"\nQuantidade de linhas duplicadas: {df_varejo_limpo.duplicated().sum()}")
# Listagem de duplicadas
print()
linhas_duplicadas = df_varejo_limpo[df_varejo_limpo.duplicated()]
print(linhas_duplicadas)
df_varejo_limpo= df_varejo_limpo.drop_duplicates()
print(f"\nQuantidade de linhas duplicadas após limpeza: {df_varejo_limpo.duplicated().sum()}")
print()
print(df_varejo_limpo.info())

#Exportando o DataFrame limpo para um novo arquivo CSV
df_varejo_limpo.to_csv('D:\\SCTEC\\Base_Varejo_Limpa.csv', index=False)