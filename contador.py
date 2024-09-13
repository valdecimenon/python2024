# Contador de palavras

texto = "python é poderoso e python é simples"

# Converte a string texto em lista
palavras = texto.split()
print(palavras)

# dicionário para contar palavras
contagem = {}

for palavra in palavras:
    # verifica se a chave (key) já está presente no dicionário
    if palavra in contagem:
        contagem[palavra] += 1  # soma 1
    else:
        contagem[palavra] = 1

print(contagem)