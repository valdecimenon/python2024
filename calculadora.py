#calculadora.py

import turtle

a = turtle.numinput('Calculadora Gráfica', 'Primeiro valor')
b = turtle.numinput('Calculadora Gráfica', 'Segundo valor')
soma = a + b

turtle.TK.messagebox.showinfo('Resultado', soma)
turtle.exitonclick()








