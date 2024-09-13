# Cria dicionário a partir de uma lista de contatos

lista_de_contatos = [
    ('João', '1234-5678'),
    ('Maria', '2345-6789'),
    ('Pedro', '3456-7890'),
    ('Ana', '4567-8901')
]


# cria o dicionário a partir da lista, usando Set Comprehension
contatos = {nome: telefone for nome, telefone in lista_de_contatos}

print(contatos)