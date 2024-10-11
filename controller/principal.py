from flask import Flask, render_template, request, redirect, url_for
from model.produto import Produto
from dao.produtoDao import *


produtoDao = ProdutoDao('banco_dados.db')
p1 = Produto('TV Samsung', 1999, 5)

# Cria uma aplicação Flask (servidor web backend)
app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = 'chave_muito_secreta'

# ====== Definição de Rotas =========

# Rota principal: página HOME
@app.route('/')
def index():
    lista = produtoDao.listar()
    return render_template('relatorio.html', titulo='Relatório de Estoque', produtos=lista)


@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html', titulo='cadastra novo produto')

@app.route('/salvar', methods=['post'])
def salvar():
    descricao =  request.form['descricao']
    preco = request.form['preco']
    quantidade = request.form['quantidade']
    # cria um objeto produto
    produto = Produto(descricao, preco, quantidade)
    produtoDao.salvar(produto)
    return redirect(url_for('index'))



if __name__ == '__main__':

    app.run(debug=True)  # para restartar automaticamente a aplicação