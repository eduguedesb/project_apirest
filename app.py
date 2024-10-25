from flask import Flask, jsonify, request, abort
from flask_restful import Api, Resource
import json

app = Flask(__name__)
api = Api(app)

# Banco de dados simulado em memória
try:
    with open('products.json') as f:
        produtos = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    produtos = {}

# Função para salvar dados no arquivo JSON
def salvar_dados():
    with open('products.json', 'w') as f:
        json.dump(produtos, f, indent=4)

# Classe para gerenciar as operações de produtos
class Produto(Resource):
    def get(self, produto_id):
        produto = produtos.get(produto_id)
        if not produto:
            abort(404, message="Produto não encontrado.")
        return jsonify(produto)

    def put(self, produto_id):
        if produto_id not in produtos:
            abort(404, message="Produto não encontrado.")
        data = request.get_json()
        produto = produtos[produto_id]
        produto['nome'] = data.get('nome', produto['nome'])
        produto['quantidade'] = data.get('quantidade', produto['quantidade'])
        produto['preco'] = data.get('preco', produto['preco'])
        salvar_dados()
        return jsonify({"message": "Produto atualizado com sucesso", "produto": produto})

    def delete(self, produto_id):
        if produto_id not in produtos:
            abort(404, message="Produto não encontrado.")
        del produtos[produto_id]
        salvar_dados()
        return jsonify({"message": "Produto removido com sucesso"})

class ListaProdutos(Resource):
    def get(self):
        return jsonify(produtos)

    def post(self):
        data = request.get_json()
        produto_id = str(len(produtos) + 1)
        novo_produto = {
            "id": produto_id,
            "nome": data['nome'],
            "quantidade": data['quantidade'],
            "preco": data['preco']
        }
        produtos[produto_id] = novo_produto
        salvar_dados()
        return jsonify({"message": "Produto adicionado com sucesso", "produto": novo_produto})

# Endpoints da API
api.add_resource(ListaProdutos, '/produtos')
api.add_resource(Produto, '/produtos/<string:produto_id>')

if __name__ == '__main__':
    app.run(debug=True)
