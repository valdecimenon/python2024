# circulos.py

import turtle as t

# muda cor do fundo
t.bgcolor('black')

#muda a velocidade
t.speed(0)

# muda a espessura da pena
t.pensize(2)

#lista de cores
cores = ['red', 'magenta', 'blue', 'cyan', 'green', 'white']

t.hideturtle()

# loop externo
for _ in range(6):
    
    # loop interno
    for cor in cores:
        #muda a cor do circulo
        t.color(cor)
        #diâmetro do circulo
        t.circle(100)
        #rotaciona 45 graus
        t.left(10)


