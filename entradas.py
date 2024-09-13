# Caixa de entrada de dados

import tkinter as tk
from tkinter import messagebox

def salvar():
    nome = str_nome.get()
    email = str_email.get()
    senha = str_senha.get()
    print(f'Nome: {nome} - E-mail: {email} - Senha: {senha}')

    arq = open('formulario.csv', 'w')
    print(f'{nome};{email};{senha}', file=arq)
    arq.close()



janela = tk.Tk()
janela.geometry("280x230")
janela.title("Formulário")

nome = tk.Label(janela, text="Nome").place(x=30, y=50)
email = tk.Label(janela, text="Email").place(x=30, y=90)
senha = tk.Label(janela, text="Senha").place(x=30, y=130)

# objetos que guardam valores tipo string ('texto')
str_nome = tk.StringVar()
str_email = tk.StringVar()
str_senha = tk.StringVar()

entrada1 = tk.Entry(janela, textvariable=str_nome).place(x=85, y=50)
entrada2 = tk.Entry(janela, textvariable=str_email).place(x=85, y=90)
entrada3 = tk.Entry(janela, textvariable=str_senha).place(x=85, y=130)

botao_salvar = tk.Button(janela, text="Salvar", command=salvar).place(x=120, y=170)
janela.mainloop()