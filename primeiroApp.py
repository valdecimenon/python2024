# .venv\scripts\activate.ps1
# pip install streamlit

# streamlit run primeiroApp.py

import streamlit as st

# Título da página - url
st.title("Primeiro App :sunglasses:")
st.image('https://softgraf.com/icones/logo_softgraf.png', width=200)

st.header('Este é um header com um divisor', divider='rainbow')
st.subheader('Este é um subheader: _Streamlit_ é :blue[legal]')
st.write('Este é um *Texto* comum')

"Texto Mágico!"
texto = "Texto na Variável"
texto

st.markdown("Markdown: *Streamlit* é **realmente** ***legal***")
st.markdown('''
    :red[Streamlit] :orange[pode] :orange[escrever]
    :blue-background[texto destacado]
''')

st.text_input("Nome:")
st.slider("Qual sua idade?", 0, 120, 25)

opcoes = st.multiselect("Selecione suas cores favoritas:",
                        ["Verde", "Amarelo", "Azul", "Vermelho"],
                        ["Amarelo", "Azul"] #seleção padrão
                        )

"Cores selecionadas"
st.write(opcoes)