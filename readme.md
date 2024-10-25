Este projeto é uma API RESTful em Python para gerenciamento de estoque de produtos, construída com Flask e Flask-RESTful. A API permite realizar operações CRUD (Create, Read, Update e Delete) para adicionar, consultar, atualizar e excluir produtos do estoque.

Funcionalidades

Criar Produto: Adiciona um novo produto ao estoque com informações como nome, quantidade e preço.
Consultar Produtos: Retorna todos os produtos do estoque ou um produto específico, através do ID.
Atualizar Produto: Atualiza informações de um produto específico (nome, quantidade, preço).
Excluir Produto: Remove um produto do estoque.

Endpoints da API
POST /produtos - Adiciona um novo produto ao estoque.
GET /produtos - Retorna todos os produtos no estoque.
GET /produtos/<produto_id> - Retorna um produto específico pelo ID.
PUT /produtos/<produto_id> - Atualiza as informações de um produto específico.
DELETE /produtos/<produto_id> - Remove um produto do estoque.

Inicialize o servidor.
A API estará acessível em http://127.0.0.1:5000.

Exemplos de Requisições:

curl -X POST http://127.0.0.1:5000/produtos -H "Content-Type: application/json" -d "{\"nome\": \"Caneta\", \"quantidade\": 100, \"preco\": 2.50}"

Consultar Produtos:
curl -X GET http://127.0.0.1:5000/produtos

Consultar Produto Específico:
curl -X GET http://127.0.0.1:5000/produtos/1

Atualizar Produto:
curl -X PUT http://127.0.0.1:5000/produtos/1 -H "Content-Type: application/json" -d "{\"nome\": \"Caneta Azul\", \"quantidade\": 150}"

Excluir Produto:
curl -X DELETE http://127.0.0.1:5000/produtos/1
