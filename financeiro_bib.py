# Biblioteca do mini sistema financeiro

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
            
