#Define funções

#Função sem argumentos
def hello():
    print('Hello World')

#Função com 2 argumentos
def somar(a, b):
    total = a + b
    print('Soma:', total)

#função com valor padrão
def mensagem(msg='Olá! Tudo bem?'):
    print(msg)

#função com 2 argumentos
def subtrair(a, b):
    r = a - b
    print('Subtração:', r)

# quantidade de parâmetros variáveis
def listar_itens(*args):
    for item in args:
        print(item)

# parâmetros variáveis nomeados
# kw = Key (chave) Value (valor)
#      'joao'     '3224-1234'
def listar_contatos(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave} = {valor}')

#---------------------------------
#Executa funções
hello()
somar(3, 4)  #parâmetros
mensagem()
mensagem('Como vai?')
#chamando função com parâmetros nomeados
subtrair(3, 4)
subtrair(b=4, a=3)
listar_itens('laranja', 'uva', 'maçã')
listar_contatos(nome='João', idade=30, cidade='Ponta Grossa')