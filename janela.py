# Usando Tkinter para criar janelas gráfica

def funcao_clicar():
    print('Botão Clicado!')


# Importa o módulo tkinter do python como tk
import tkinter as tk

# Cria a janela principal
root = tk.Tk()

# Define o título da janela
root.title("Titulo da janela")

# Tamanho inicial 
root.geometry("640x480")

# Cria uma botão
botao = tk.Button(root, text='Clique aqui', command=funcao_clicar)

# Adiciona o botão na janela
botao.pack(pady=20)  #padding y = afastamento do topo até o botão

# Inicia o loop principal
root.mainloop()