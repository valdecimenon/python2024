# Conjunto é uma coleção de elementos que não possui duplicatas
# e não tem ordem

# Criando um conjunto com chaves
conjunto = {1, 1, 2, 3, 4, 5, 5, 6, 6}
print(conjunto)

# Criando um conjunto com a função set()
conjunto2 = set({2,2, 3, 4, 5, 5})
print(conjunto2)

# Criando um conjunto a partir de uma string
conjunto3 = set('abracadabra')
print(conjunto3)

# Adicionando elementos
conjunto = {1, 2, 3}
conjunto.add(4)
print(conjunto)

# Removendo
conjunto.remove(2)
print(conjunto)

# Erro: elemento não existe
#conjunto.remove(2)

# Removendo com discard() = não dá erro se elemento não existir
conjunto.discard(2)

#  Conversão lista para conjunto
lista = [1, 2, 2, 3, 3, 4]
conjunto = set(lista)
print(conjunto)

# Convertendo de conjunto para lista
lista = list(conjunto)
print(lista)

# Verifica se um item está no conjunto
conjunto = {1,2,3,4}
print(3 in conjunto)
print(6 not in conjunto)

# União de conjunto
conj1 = {1, 2, 3, 4, 5}
conj2 = {4, 5, 6, 7, 8}
uniao = conj1.union(conj2)
# OU
uniao = conj1 | conj2
print('União:', uniao)

# Interseção
intersecao = conj1.intersection(conj2)
# OU
intersecao = conj1 & conj2
print(intersecao)

# Diferença
diferenca = conj1.difference(conj2)
# OU
diferenca = conj1 - conj2
print(diferenca)

##### List Comprehension = Compreensão de Listas

# Elevar ao quadrado cada valor da lista
lista = [1, 2, 3, 4] 
lista2 = []

for x in lista:
    lista2.append(x ** 2)

print(lista2)

# Usando List Comprehension
lista2 = [x ** 2 for x in lista]
print(lista2)

#### Set Comprehension
conjunto = {x for x in 'abracadabra' if not x in 'abc'}
print(conjunto)