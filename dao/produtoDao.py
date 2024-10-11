# Obs: vamos usar a coluna rowid do SQLITE3 como id
import sqlite3

from model.produto import Produto

SQL_CRIAR_TABELA = '''CREATE TABLE IF NOT EXISTS produto
                      (descricao VARCHAR(255) NOT NULL,
                       preco DOUBLE NOT NULL,
                       quantidade INTEGER NOT NULL
                      )
                      '''

SQL_SALVAR_PRODUTO = 'INSERT INTO produto VALUES (?, ?, ?)'

SQL_LISTAR_PRODUTOS = 'SELECT descricao, preco, quantidade, rowid FROM produto'

SQL_PRODUTO_POR_COD = 'SELECT descricao, preco, quantidade, rowid FROM produto WHERE rowid=?'

SQL_ATUALIZAR_PRODUTO = 'UPDATE produto SET descricao=?, preco=?, quantidade=? WHERE rowid=?'

SQL_DELETAR_PRODUTO = 'DELETE FROM produto WHERE rowid=?'


class ProdutoDao:

    def __init__(self, nome_banco):
        self.__nome_banco = nome_banco
        self.criar_tabela()

    def criar_tabela(self):
        print('Conectando banco de dados...', end='')
        conexao = sqlite3.connect(self.__nome_banco)
        # obtém um cursor para executar comandos SQL
        cursor = conexao.cursor()
        cursor.execute(SQL_CRIAR_TABELA)
        #confirma operação
        conexao.commit()
        print('OK')

    def salvar(self, produto):
        print('Salvando produto...', end='')
        conexao = sqlite3.connect(self.__nome_banco)
        cursor = conexao.cursor()
        cursor.execute(SQL_SALVAR_PRODUTO, (produto.descricao, produto.preco, produto.quantidade))
        produto.cod = cursor.lastrowid
        conexao.commit()  # confirmação
        print('OK')
        return produto

    def listar(self):
        conexao = sqlite3.connect(self.__nome_banco)
        cursor = conexao.cursor()
        # seleciona todos os produtos no banco
        cursor.execute(SQL_LISTAR_PRODUTOS)
        # busca o produtos selecionados
        return converte_produtos(cursor.fetchall())

    def buscar_por_cod(self, cod):
        conexao = sqlite3.connect(self.__nome_banco)
        cursor = conexao.cursor()
        cursor.execute(SQL_PRODUTO_POR_COD, [cod])
        # devole tupla contendo apenas um produto
        tupla = cursor.fetchone()
        if tupla:
            return tupla2produto(tupla)
        return None

    def deletar(self, cod):
        conexao = sqlite3.connect(self.__nome_banco)
        cursor = conexao.cursor()
        cursor.execute(SQL_DELETAR_PRODUTO, [cod])
        conexao.commit()

    def atualizar(self, p):
        print('Atualizando produto...', end='')
        conexao = sqlite3.connect(self.__nome_banco)
        cursor = conexao.cursor()
        cursor.execute(SQL_ATUALIZAR_PRODUTO, [p.descricao,
                                               p.preco,
                                               p.quantidade,
                                               p.cod
                                               ])
        conexao.commit()
        print('OK')
        return p






def tupla2produto(tupla):
    return Produto(tupla[0], tupla[1], tupla[2], tupla[3])

def converte_produtos(lista):
    return list(map(tupla2produto, lista))
