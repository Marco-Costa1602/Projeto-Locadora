from flask import Flask, jsonify, request
from main import query, execute
from serializer import genero_name_web, genero_name_db, diretor_name_web, diretor_name_db
from validacao import valida_genero, valida_diretor
from models import insert_genero, get_genero, delete_genero, update_genero, get_diretor, insert_diretor, delete_diretor, update_diretor


#Serializer serve para validação e formatação

app = Flask(__name__)

tabelas = ('filmes', 'generos', 'locacoes', 'pagamento', 'usuarios', 'diretores')


#########################################################################
######################################################################### CONTROLER - GÊNEROS
# Função para buscar dados nas tabelas.
@app.route("/generos", methods=["GET", "POST", "DELETE", "PATCH"])
def controller_genero():
    if request.method == "POST":
        genero = genero_name_web(**request.json)
        if valida_genero(**genero):
            insert_genero(**genero)
            genero_criado = get_genero(genero["nome"])
            return jsonify(genero_name_db(genero_criado))
        else:
            return jsonify({"Erro": "Genero inválido ou já inserido!"})

    if request.method == "GET":
        return jsonify(get_genero(**request.json))

    if request.method == "DELETE":
        delete_genero(**request.json)
        return jsonify(get_genero(**request.json))

    if request.method == "PATCH":
        update_genero(request.json['nome'], request.json['novo'])
        return jsonify(get_genero(request.json["novo"]))


#########################################################################
######################################################################### CONTROLLER - DIRETORES
@app.route("/diretores", methods=["GET", "POST", "DELETE", "PATCH"])
def controller_diretores():
    if request.method == "GET":
        return jsonify(get_diretor(**request.json))

    if request.method == "POST":
        diretor = diretor_name_web(**request.json)
        if valida_diretor(**diretor):
            insert_diretor(**diretor)
            diretor_criado = get_diretor(diretor["nome_completo"])
            return jsonify(diretor_name_db(diretor_criado))
        else:
            return jsonify({"Erro": "Diretor inválido ou já inserido!"})

    if request.method == "DELETE":
        delete_diretor(**request.json)
        return jsonify(get_diretor(**request.json))

    if request.method == "PATCH":
        update_diretor(**request.json)
        return jsonify(get_diretor(request.json["novo"]))

#########################################################################
######################################################################### CONTROLLER - FILMES



if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)

# jsonify({"metodo": request.method})

