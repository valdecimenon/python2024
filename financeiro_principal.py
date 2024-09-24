
# Importa a classe Lancamento e funções
from financeiro_bib import *

# Variáveis do sistema
SAIR = 6
lista_lancamentos = []

# Mostra o menu principal da aplicação
def menu():
    print('\n\n======= Controle Financeiro ========')
    print('[1] Novo Lançamento')
    print('[2] Listar Lançamentos')
    print('[3] Calcular total de lançamentos')
    print('[4] Exportar para o Excel')
    print('[5] Importar do Excel')
    print('[6] Sair')

    opcao = 0
    while (opcao < 1 or opcao > SAIR):
        opcao = int(input('\nQual opção?'))
    
    return opcao

# Cria e salva novo lançamento em lista_lancamentos
def novo_lancamento():
    valor = float(input('Valor em R$: '))
    data = input('Data (dd/mm/aaaa):')
    Lancamento.mostra_categorias()
    categoria = int(input('Número da categoria:'))
    descricao = input('Descrição: ')
    lancamento = Lancamento(valor, data, categoria, descricao)
    lista_lancamentos.append(lancamento)
    print('Novo Lançamento foi criado')


# Lista todos os lançamentos já cadastrados
def listar_lancamentos():
    if len(lista_lancamentos) == 0:
        print('Ainda não há nenhum lançamento cadastrado')
    else:
        for item in lista_lancamentos:
            print(item)

# Soma todos os lançamentos
def total_lancamentos():
    total = 0
    for item in lista_lancamentos:
        total += item.valor
    print(f'Total de lançamentos: R$ {total:.2f}')


# Testes
if __name__ == '__main__':
    escolha = 0

    # enquanto não sair
    while (escolha != SAIR):
        escolha = menu()

        if escolha == 1:
            novo_lancamento()

        elif escolha == 2:
            listar_lancamentos()

        elif escolha == 3:
            total_lancamentos()
    
        elif escolha == 4:
            print('---- Salvando em CSV -----')
            gravar_csv(lista_lancamentos)
    
        elif escolha == 5:
            print('---- Importando CSV -----')
            lista_lancamentos = ler_csv()
    
        else:
            print('Adeus')
    
    