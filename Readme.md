# Mini Projeto de Análise de Dados de Varejo

Este projeto realiza o carregamento, a limpeza, o tratamento e a análise exploratória de uma base de dados de varejo utilizando a biblioteca **Pandas** em Python. 

O objetivo principal é verificar e ajustar inconsistências estruturais na base de dados e extrair dados sobre o perfil dos clientes, focando na distribuição da quantidade de filhos (`CL_FHL`) cruzada com outras variáveis.

---

## Estrutura do Script

O script está dividido logicamente nas seguintes etapas estruturadas:

1. **Carga dos Dados**: Importação do arquivo delimitado `Base Varejo.csv` e inspeção inicial das dimensões e tipos de dados.
2. **Limpeza de Inconsistências**:
   * Remoção de colunas sobressalentes e vazias.
   * Eliminação de espaços em branco e padronização de strings na coluna de categoria de produtos (`PR_CAT`).
   * Conversão e normalização de strings de datas para o formato nativo `datetime`.
   * Tratamento de campos de texto vazios ocultos, convertendo-os para o formato padrão `NaN` (Not a Number).
   * Identificação e remoção de registros completamente duplicados.
3. **Exportação**: Salvamento dos dados limpos em um novo arquivo CSV (`Base_Varejo_Limpa.csv`).
4. **Análise de Clientes**:
   * Filtragem de clientes únicos (`CL_ID`) mantendo a linha correspondente ao seu valor máximo de filhos cadastrado.
   * Cálculo de métricas descritivas completas para a coluna de filhos (Média, Mediana, Moda, Desvio Padrão e Quartis).
   * **Análise Multivariada**: Geração de tabelas cruzando o número de filhos (`CL_FHL`) com Gênero (`CL_GENERO`), Estado Civil (`CL_EC`) e Classe Social do cliente (`CL_SEG`).

---

## Tecnologias e Bibliotecas Utilizadas

* **Python 3.x**
* **Pandas**: Para manipulação, limpeza e agregação de dados.
* **NumPy**: Para operações matemáticas e substituição eficiente de valores nulos estruturais.

---


## Como rodar o programa completo:

Como rodar o programa completo:

* Baixe o código via Git clone
* Baixe as dependencias via comando `pip install -r requirements.txt`
* Execute o script principal:


```Bash

python MiniProjeto_MarcoOlinger_AnaliseDeDados_Turma1.py

```


## Outputs Gerados no Console
Ao executar o script, as seguintes informações enriquecidas são exibidas no console:

* Relatórios de diagnóstico de nulos e duplicados antes/depois da limpeza.
* Tabela descritiva contendo a contagem absoluta de clientes segmentados estritamente pela quantidade de filhos.
* Matriz de contagem analítica cruzada detalhando o volume de clientes por características combinadas:
---

## Estrutura do Projeto

O script espera e manipula a seguinte estrutura de arquivos no diretório especificado (`D:\SCTEC\`):

```text
D:\SCTEC\
│
├── Base Varejo.csv                          # Base de dados bruta original (Entrada)
├── Base_Varejo_Limpa.csv                    # Base de dados tratada (Gerada pelo script)
└── MiniProjeto_MarcoOlinger_AnaliseDeDados_Turma1.py  # Script principal de execução


