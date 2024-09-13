def desenha_linhas(x, cor):
    y = 20
    for _ in range(30):
        canvas.create_line(x, y, x+100, y, fill=cor)
        y += 20


# Programa de desenho

import tkinter as tk

janela = tk.Tk()

# tela gráfico de desenho
canvas = tk.Canvas(janela, width=1200, height=640)

# Adiciona o canvas na janela
canvas.pack()

# Para desenhar uma linha no canvas: create_line (ponto1, ponto2, cor) 
#                 x1, y1, x2, y2

# repete horizontalmente
x = 0
for _ in range(10):
    desenha_linhas(x, 'red')
    x += 110



janela.mainloop()