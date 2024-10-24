import streamlit as st
import pandas as pd

# Aba da página
st.set_page_config(
    page_title="Controle de Estoque",
    page_icon=":shopping_trolley:",
)

# Função para adicionar um novo produto
def cadastra_produto():
    produto_id = st.text_input("ID")
    produto_nome = st.text_input("Nome")
    produto_preco = st.number_input("Preço", min_value=0.0)
    produto_estoque = st.number_input("Estoque", min_value=0)

    if st.button("Cadastrar Produto"):
        # Cria novo DataFrame para o novo produto
        novo_produto = pd.DataFrame({
            'ID': [produto_id],
            'Nome': [produto_nome],
            'Preco': [produto_preco],
            'Estoque': [produto_estoque]
        })

        # Usa pd.concat() para adicionar o DataFrame novo_produto ao DataFrame existente
        st.session_state['produtos'] = pd.concat([st.session_state['produtos'], novo_produto], ignore_index=True)
        st.success("Produto cadastro com sucesso!")


# Função para alterar um produto existente
def alterar_produto():
    # Converte a coluna ID em uma lista
    lista_produtos = st.session_state['produtos']['ID'].tolist()
    # Cria uma caixa de seleção com a lista de IDs
    produto_id = st.selectbox("Selecione ID do Produto para Alterar", lista_produtos)

    if produto_id:
        # Localiza o produto pelo ID
        produto = st.session_state['produtos'][st.session_state['produtos']['ID'] == produto_id].iloc[0]

        # Entrada de dados para atualizar o produto
        novo_nome = st.text_input("Nome", value=produto['Nome'])
        novo_preco = st.number_input("Preço", min_value=0.0, value=produto['Preco'])
        novo_estoque = st.number_input("Estoque", min_value=0, value=int(produto['Estoque']))

        if st.button("Atualizar Produto"):
            # Atualiza as informações no DataFrame
            st.session_state['produtos'].loc[
                st.session_state['produtos']['ID'] == produto_id, ['Nome', 'Preco', 'Estoque']] = \
                                                              [novo_nome, novo_preco, novo_estoque]
            st.success("Produto atualizado com sucesso!")


# Função para deletar um produto
def apagar_produto():
    lista_produtos = st.session_state['produtos']['ID'].tolist()
    produto_id = st.selectbox("Selecione ID do Produto para Apagar", lista_produtos)

    if produto_id:
        if st.button("Apagar Produto"):
            # Remove o produto pelo ID
            st.session_state['produtos'] = st.session_state['produtos'][
                st.session_state['produtos']['ID'] != produto_id]
            st.success("Produto apagado com sucesso!")


# Função para mostrar os produtos
def listar_produtos():
    st.subheader("Todos os Produtos do Sistema")
    st.dataframe(st.session_state['produtos'])


# ===== Programa Principal =====
if __name__ == "__main__":
    st.title("Controle de Estoque")

    # Inicializa o DataFrame e salva na sessão
    if 'produtos' not in st.session_state:
        st.session_state['produtos'] = pd.DataFrame(columns=['ID', 'Nome', 'Preco', 'Estoque'])

    # Controle da ação através da barra lateral
    opcao = st.sidebar.selectbox("Escolha uma opção",
                                 ["Cadastrar Produto", "Alterar Produto", "Apagar Produto", "Listar Todos os Produtos"])

    if opcao == "Cadastrar Produto":
        cadastra_produto()
    elif opcao == "Alterar Produto":
        alterar_produto()
    elif opcao == "Apagar Produto":
        apagar_produto()
    elif opcao == "Listar Todos os Produtos":
        listar_produtos()
