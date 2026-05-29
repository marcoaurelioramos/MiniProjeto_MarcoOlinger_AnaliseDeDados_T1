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

print()
print('################################################################################')

#Agrupamento dos dados por cliente para análise da quantidade de filhos (CL_ID) e a quantidade de filhos (CL_FHL)
df_cli_agrupado = df_varejo_limpo.sort_values(by=['CL_ID', 'CL_FHL'], ascending=[True, False]).drop_duplicates(subset=['CL_ID'])

# Exibir o resultado
print(df_cli_agrupado)

print('################################################################################') 


print('Análise estatística da coluna CL_FHL')
if 'CL_FHL' in df_cli_agrupado.columns:
    estatisticas_filhos = df_cli_agrupado['CL_FHL'].describe()
    moda_filhos = df_cli_agrupado['CL_FHL'].mode()[0]
    
    print(f"Contagem: {estatisticas_filhos['count']}")
    print(f"Média: {estatisticas_filhos['mean']:.2f}")
    print(f"Mediana: {df_cli_agrupado['CL_FHL'].median()}")
    print(f"Moda: {moda_filhos}")
    print(f"Desvio Padrão: {estatisticas_filhos['std']:.2f}")
    print(f"Mínimo: {estatisticas_filhos['min']}")
    print(f"Quartil 25%: {estatisticas_filhos['25%']}")
    print(f"Quartil 50% (Mediana): {estatisticas_filhos['50%']}")
    print(f"Quartil 75%: {estatisticas_filhos['75%']}")
    print(f"Máximo: {estatisticas_filhos['max']}")

# Contagem de clientes por número de filhos
df_contagem_fhl = df_cli_agrupado['CL_FHL'].value_counts().sort_index()
df_contagem_fhl = df_contagem_fhl.reset_index()
print("\nContagem de clientes por número de filhos:")
df_contagem_fhl.columns = ['Quantidade_de_CL_FHL', 'Total_de_Clientes_ID']
df_contagem_fhl = df_contagem_fhl.sort_values(by='Quantidade_de_CL_FHL') 
print(df_contagem_fhl) 

print()
print('################################################################################')

# 1. Faz a contagem passando a lista de colunas (sem o as_index)
df_cruzado = df_cli_agrupado[['CL_FHL', 'CL_GENERO', 'CL_EC', 'CL_SEG']].value_counts()

# 2. Transforma o resultado em DataFrame de forma segura
df_cruzado = df_cruzado.reset_index()

# 3. Ajusta o nome da coluna de contagem (o Pandas antigo costumava chamá-la de 0 ou 'size')
# Esse comando garante que, não importa o nome antigo, ela vire 'Total_de_Clientes'
df_cruzado.columns = ['CL_FHL', 'CL_GENERO', 'CL_EC', 'CL_SEG', 'Total_de_Clientes']

# 4. Ordena pela quantidade de filhos
df_cruzado = df_cruzado.sort_values(by='CL_FHL')

print("\nContagem detalhada de clientes:")
print(df_cruzado)