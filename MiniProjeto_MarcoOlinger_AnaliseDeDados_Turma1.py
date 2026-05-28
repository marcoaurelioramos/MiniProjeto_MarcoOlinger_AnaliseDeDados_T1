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

# Verificação de linhas com campos  vazios
# 1. Transformar espaço em branco em NaN real
df_varejo_analise = df_varejo.replace(r'^\s*$', np.nan, regex=True)

# 2. Exibir o total real de campos vazios por coluna
print("Total de vazios por coluna:")
print(df_varejo_analise.isna().sum())

# Remoção de linhas duplicadas
print(f"\nQuantidade de linhas duplicadas: {df_varejo.duplicated().sum()}")
# Listagem de duplicadas
# Mostra todas as linhas duplicadas (mantendo a primeira ocorrência oculta)
linhas_duplicadas = df_varejo[df_varejo.duplicated()]
print(linhas_duplicadas)
print('')
print('Análise estatística da coluna CL_FHL')
if 'CL_FHL' in df_varejo.columns:
    estatisticas_filhos = df_varejo['CL_FHL'].describe()
    moda_filhos = df_varejo['CL_FHL'].mode()[0]
    
    print(f"Contagem: {estatisticas_filhos['count']}")
    print(f"Média: {estatisticas_filhos['mean']:.2f}")
    print(f"Mediana: {df_varejo['CL_FHL'].median()}")
    print(f"Moda: {moda_filhos}")
    print(f"Desvio Padrão: {estatisticas_filhos['std']:.2f}")
    print(f"Mínimo: {estatisticas_filhos['min']}")
    print(f"Quartil 25%: {estatisticas_filhos['25%']}")
    print(f"Quartil 50% (Mediana): {estatisticas_filhos['50%']}")
    print(f"Quartil 75%: {estatisticas_filhos['75%']}")
    print(f"Máximo: {estatisticas_filhos['max']}")