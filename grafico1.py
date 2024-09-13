# Aula 01 - Primeiro programa
# grafico1.py

#importa pacote
import turtle

#cria objeto turtle
t = turtle.Turtle()

#desenha triangulo
for x in range(3):
    t.forward(100)  #anda para frente 100 unidades
    t.left(120)     #rotaciona para a esquerda 120 graus

# finaliza
turtle.done()
