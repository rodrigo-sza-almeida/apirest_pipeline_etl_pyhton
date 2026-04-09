# Bibliotecas que serão utilizadas para criar a API, criar o túnel e manipular os dados dos clientes

from flask import Flask, make_response, jsonify, request 
from pyngrok import ngrok
from bd import Clientes

# Criando a aplicação Flask e configurando para não ordenar as chaves do JSON

app = Flask(__name__)
app.json.sort_keys = False

# Configurando o token de autenticação do ngrok para criar o túnel e expor a API na internet

NGROK_AUTH_TOKEN = "NGROK-KEY"  # Substitua pelo seu token de autenticação do ngrok
ngrok.set_auth_token(NGROK_AUTH_TOKEN)

# Rota para obter a lista de clientes do banco de dados (GET)

@app.route("/clientes_banco", methods = ["GET"])
def get_clientes():
    return make_response(jsonify(Clientes)) # Retorna a lista de clientes em formato JSON com status 200 (OK)


# Rota para obter um cliente específico por ID (GET)

@app.route("/clientes_banco/<int:id>", methods=["GET"])
def get_cliente_por_id(id):
    cliente = next((c for c in Clientes if c["id"] == id), None)
    if cliente:
        return make_response(jsonify(cliente), 200)
    return make_response(jsonify({"erro": "Cliente não encontrado"}), 404)


# Rota para criar um novo cliente no banco de dados (POST)

@app.route("/clientes_banco/", methods = ["POST"])
def create_clientes():
    clientes = request.json
    Clientes.append(clientes)
    return make_response(jsonify(clientes), 201)


# Rota para atualizar as informações de um cliente existente (PUT)

@app.route("/clientes_banco/<int:id>", methods=["PUT"])
def update_cliente(id):
    cliente = next((c for c in Clientes if c["id"] == id), None)
    if not cliente:
        return make_response(jsonify({"erro": "Cliente não encontrado"}), 404)
    
    dados_atualizados = request.json

    # Atualiza as informações do dicionário encontrado

    cliente.update(dados_atualizados)
    
    return make_response(jsonify(cliente), 200)


# Rota para remover um cliente do banco de dados (DELETE)

@app.route("/clientes_banco/<int:id>", methods=["DELETE"])
def delete_cliente(id):
    cliente = next((c for c in Clientes if c["id"] == id), None)
    if not cliente:
        return make_response(jsonify({"erro": "Cliente não encontrado"}), 404)
    
    # Remove o cliente da lista de clientes
    
    Clientes.remove(cliente)
    return make_response(jsonify({"mensagem": "Cliente removido com sucesso"}), 200)



# Inicia a aplicação Flask e o túnel ngrok para expor a API na internet

if __name__ == '__main__':
    # Cria o túnel na porta 5000
    public_url = ngrok.connect(5000).public_url
    print(f" * API disponível em: {public_url}")
    app.run(port=5000)