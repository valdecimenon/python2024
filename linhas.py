# linhas.py

from turtle import *

#cria um objeto Turtle
t = Turtle()

#cria um objeto tela
s = Screen()

#muda cor de fundo
s.bgcolor('black')

#muda cor da caneta
pencolor('red')

dist = 0
rot = 0

#velocidade
speed(0)

# levanta a caneta
penup()

#desloca a tartaruga, para cima, 200 unidades
#    x   y
goto(0, 200)

# baixa a caneta
pendown()

# loop infinito
while (True):
    #move o cursor para frente
    forward(dist)
    #rotaciona para a direita
    right(rot)
    # incrementa variáveis
    dist += 3  #a = a + 3
    rot += 1
    # interrompe o lop depois de 210 execuções
    if rot == 210:
        break

done()

