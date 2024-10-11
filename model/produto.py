class Produto:

    # construtor ou inicializador da classe
    def __init__(self, descricao, preco, quantidade, cod=None):
        self.__cod = cod
        self.__descricao = descricao
        self.__preco = preco
        self.__quantidade = quantidade

    def __str__(self):
        return f'ID: {self.__cod} \tDescrição: {self.__descricao} \tPreco: R$ {self.__preco:.2f} \tQuantidade: {self.__quantidade}'

    # Métodos para leitura das variáveis
    @property
    def cod(self):
        return self.__cod

    @property
    def preco(self):
        return self.__preco

    @property
    def quantidade(self):
        return self.__quantidade

    @property
    def descricao(self):
        return self.__descricao

    # Métodos para alteração das variáveis
    @cod.setter
    def cod(self, cod):
        self.__cod = cod

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

