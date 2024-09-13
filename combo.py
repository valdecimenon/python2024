import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.geometry("640x480")

# cria uma variável tipo string do tkinter
var_string = tk.StringVar()
combobox = ttk.Combobox(janela, textvariable=var_string, 
                        values=["Python", "Java", "Javascript"])
combobox.pack()

janela.mainloop()

print(var_string.get())