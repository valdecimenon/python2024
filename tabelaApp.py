import streamlit as st
import pandas as pd

# Titulo do aplicativo
st.title('Lista de Produtos')

# Cria um dicionário para simulação de dados
dados = {
    'Nome do Produto' : ['Teclado', 'Mouse', 'Monitor', 'Processador'],
    'Descrição' : ['Teclado mecânico', 'Mouse sem fio', 'Monitor 24 pol.', 'i7'],
    'Preço' : [199.99, 99.99, 899.99, 1299.99],
    'Quantidade em Estoque' : [10, 15, 5, 12]
}

# Converte dicionário em DataFrame
df1 = pd.DataFrame(dados)

# Exibe o DataFrame
st.subheader('DataFrame a partir do dicionário de dados')
st.dataframe(df1)

# Define URL do arquivo do Excel
url = 'https://softgraf.com/cursodatascience/produtos.xlsx'

# Lê o arquivo da url e converte em um DataFrame
df2 = pd.read_excel(url, engine='openpyxl')

# Exibe o DataFrame
st.subheader('DataFrame a partir do arquivo do Excel')
st.dataframe(df2)


