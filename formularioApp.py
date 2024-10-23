# buscar: streamlit emoji shortcodes

import streamlit as st

# Valores default
nome = ''
preco = 0.00
estoque = 10

# Configurações da página
st.set_page_config (
    page_title="Cadastro de Produtos",
    page_icon=":shopping_trolley:"
    # layout="wide"
)

st.title("Cadastrar")
st.subheader("Formulário para cadastrar produtos")

# Cria o formulário
with st.form(key="form_produto"):
    nome = st.text_input('Nome do Produto', max_chars=60, placeholder='Nome com descrição do produto', value=nome)
    preco = st.number_input('Preço do Produto', min_value=0.00, step=0.01, value=preco)
    estoque = st.number_input('Quantidade em Estoque', min_value=0, step=1, value=estoque)

    # True ou False
    enviou = st.form_submit_button(label='Cadastrar')


# Ação quando o formulário é enviado
if enviou:
    st.success('Produto cadastrado com sucesso!')
    st.write(f'**Nome:** {nome}')
    st.write(f'**Preço:** R$ {preco}')
    st.write(f'**Quantidade em Estoque:** {estoque}')