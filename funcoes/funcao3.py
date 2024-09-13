#programação estruturada

def somar(a, b):
    s = a + b
    return s

print(somar(1,2))

#programação funcional => lambda = função anônina
# não tem variáveis, apenas constantes
# funções são anônimas
# uma função pode receber outra função
# uma função pode retornar outra função

# No python, um lambda é uma função anônima de uma única linha
# lambda var1, var2: código
soma = lambda a, b: a + b
print(soma(3,4))


# função map()
# aplica uma função a todos os itens de um iterável (lista, tupla) e
# retorna um iterador com os resultados
def quadrado(x):
    return x ** 2  #x elevado ao quadrado

numeros = [1, 2, 3, 4, 5, 6]
quad = []

print('Exemplo usando for')
for x in numeros:
    quad.append(quadrado(x))

print(quad)

print('Exemplo usando map - com função')
quadrados = list(map(quadrado, numeros))
print(quadrados)

print('Exemplo usando map - com lambda')
quadrados = list(map(lambda x: x ** 2, numeros))
print(quadrados)

# função filter: filtra itens, matendo somente os itens que corresponde a uma condição
pares = list(filter(lambda x: x % 2 == 0, numeros))
print('Filtrando os pares')
print(pares)





