
lista1 = [1, 2, -8]
lista2 = [0, -5, 18, 1, 7, 10]

#função para somar os valores de uma lista
def somar(lista):
    soma = 0
    for x in lista:
        soma += x
    return soma

#função para multiplicar os valores de uma lista
def multiplicar(lista):
    total = 1
    for x in lista:
        total *= x
    return total

# função para obter o maior número de uma lista
def maior(lista):
    maior = lista[0]
    for x in lista:
        if x > maior:
            maior = x
    return maior


# função para obter o menor número de uma lista
def menor(lista):
    menor = lista[0]
    for x in lista:
        if x < menor:
            menor = x
    return menor



# programa principal
if __name__ == '__main__':
    print(somar(lista1))
    print(somar(lista2))


