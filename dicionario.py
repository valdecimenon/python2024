# Dicionário é uma coleção desordenada de pares chave : valor
# Chave não pode ser duplicada, mas o valor pode

# Criando um dicionário
pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "Ponta Grossa"
}

print(pessoa)
print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["cidade"])

# Adicionando uma chave
pessoa["profissao"] = "Programador"

# Alterando
pessoa["idade"] = 33

# Removendo um item usando pop() = retorna o item removido
idade = pessoa.pop("idade")

# Removendo usando del
del pessoa["cidade"]

print(pessoa)

### Métodos úteis do dicionário ###
# Lista todas as chaves
print(pessoa.keys())

# Retorna uma lista de valores
print(pessoa.values())

# Retorna uma lista de tuplas (chave: valor)
print(pessoa.items())