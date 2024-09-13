# Funções quanto ao retorno

# função sem retorno
def calcular(a, b, c):
    resultado = a + b - c
    print('Executou função sem retorno:', resultado)

# função com retorno
def calculos(a, b, c):
    resultado = a + b - c
    return resultado 

# Quanto à organização do código
# Função aninhada

# Neste exemplo o parâmetro 'a' pertence à função externa,
# porém é usado pela função interna, esse tipo de variável
# possui ESCOPO ENCLOSING
def funcao_externa(a):
    print('a=', a)   # 10

    def funcao_interna(b):
        print('b=', b)  #5
        return a + b

    return funcao_interna

#--------------------------------------------
# Executa as funções
calcular(4, 5, 3)

r = calculos(4, 5, 3)
print('Executou função com retorno:', r)

somar = funcao_externa(10)
r = somar(5)
print(r)