# espiral.py


# importa todas as funções do módulo
from turtle import *

#cor do fundo
bgcolor('black')

speed(0)

hideturtle()


for i in range(360):
    color('red')
    # desenha o círculo vermelho
    circle(i)
    color('orange')

    #desenha o círculo laranha com 80% do anterior
    circle(i * 0.8)

    #move o cursor 3 unidades para a direita
    right(3)

    #e 3 unidades para frente
    forward(3)

#finaliza
done()


    
    
