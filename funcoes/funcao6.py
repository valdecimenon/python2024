# Funções built-in (embutidas)
# são funções que são importadas automaticamente
# para serem usadas em qualquer local

# Exemplos:

print(type(5))
print(type(5.0))
print(type('5'))

lista = [1,2,3,4,5]
print(sum(lista))
print(min(lista))
print(max(lista))

# outros:
# abs(-10) = 10
# round(3.7) = 4 
# pow(2, 3) = 8

print(bin(255))    #0b11111111
print(oct(255))    #0o377
print(hex(255))    #0xff

frutas = ['jaca', 'tomate', 'tangerina', 'banana', 'coco', 'caju']
copia = sorted(frutas)
print(copia)
print(list(reversed(copia)))

print('enumerate')
lista = ['a', 'b', 'c']
# após enumerate = [(0, 'a'), (1, 'b'), (2, 'c')]
for indice,  valor in enumerate(lista):
    print(indice, valor)

# função eval(): evolui uma expressão em python
a = eval("2+2")
print('a=', a)

eval('print("hello")')

print('=== meu terminal python ===')
#terminal = input('>>>')   #print("hello")

#eval(terminal)

print(len('texto')) #5
print('texto'.upper())
print('TEXTO'.lower())
print('Python é da hora!'.split())