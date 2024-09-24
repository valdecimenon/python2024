# Biblioteca do mini sistema financeiro

import csv

# representa um laçamento no sistema
class Lancamento:

    # variável estática (armazenada na classe, não aos objetos)
    #                    0               1          2                3
    categorias = ['comida/bebidas', 'compras', 'transportes', 'entretenimento',
    #                 4         5        6          7
                  'família', 'saúde', 'viagens', 'outros']

    # inicializador 
    def __init__(self, valor, data, categoria, descricao):
        self.valor = valor
        self.data = data
        self.categoria = categoria
        self.descricao = descricao

    @staticmethod
    def mostra_categorias():
        for ind, item in enumerate(Lancamento.categorias):
            print(ind, '=', item)

    def __str__(self):
        categoria = Lancamento.categorias[self.categoria]
        return f'R$ {self.valor:.2f} Data: {self.data} Categoria: {categoria} Descrição: {self.descricao}'
    
    # Método para retornar os dados do lançamento em forma de tupla
    # Ex: (100, '19/09/2024', 0, 'compras supermercado')
    def para_tupla(self):
        return self.valor, self.data, self.categoria, self.descricao

#=====================================================================

# Função para cnoverter uma lista de lançamentos em uma tupla de lançamentos
# ( (100, '19/09/2024', 0, 'compras supermercado'), (200, '20/09/2024', 1, 'gastos'))
def lista_para_tupla(lista_lancamentos):
    # enhanced for
    return tuple(item.para_tupla() for item in lista_lancamentos)
        

# Função para salvar a lista de lançamentos em formato csv do Excel
def gravar_csv(lista_lancamentos):
    arquivo = open('lancamentos.csv', 'w', newline='', encoding='UTF-8')
    saida = csv.writer(arquivo, delimiter=';')
    saida.writerows(lista_para_tupla(lista_lancamentos))
    arquivo.close()

# Importa os dados do arquivo .csv e retorna em formato de lista de lancamentos
def ler_csv():
    arquivo = open('lancamentos.csv', 'r', encoding='UTF-8')
    dados = csv.reader(arquivo, delimiter=';')
    lista = []
    # cada item é um lançamento, porém com dados em formato string, que serão convertidos abaixo
    for item in dados:
        valor = float(item[0])
        data = item[1]
        categoria = int(item[2])
        descricao = item[3]
        # cria objeto lancamento
        lancamento = Lancamento(valor, data, categoria, descricao)
        # salva objeto na lista temporária
        lista.append(lancamento)
    arquivo.close()
    return lista