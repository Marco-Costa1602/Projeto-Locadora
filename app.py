from flask import Flask, jsonify, request
from serializer import genero_name_web, genero_name_db, diretor_name_web, diretor_name_db, nome_diretor_from_web, titulo_filme_from_web, filme_name_web, filme_name_db, usuario_from_web, usuario_from_db, nome_usuario_from_web, nome_genero_from_web
from validacao import valida_genero, valida_diretor, valida_filme, valida_usuario
from models import insert_genero, get_genero, select_genero, delete_genero, update_genero, get_diretor, select_diretor, insert_diretor, delete_diretor, update_diretor, select_filme, delete_fime, update_filme, get_filme, insert_filme, get_usuario, select_usuarios, delete_usuario, update_usuario, insert_usuario

app = Flask(__name__)


#########################################################################
######################################################################### CONTROLER - GÊNEROS
@app.route("/generos", methods=["POST"]) #Check
def inserir_genero():
    genero = genero_name_web(**request.json)
    if valida_genero(**genero):
        id_genero = insert_genero(**genero)
        genero_cadastrado = get_genero(id_genero)
        return jsonify(genero_name_db(genero_cadastrado))
    else:
        return jsonify({"erro": "Gênero inválido ou já inserido!"})


@app.route("/generos/<int:id>", methods=["PUT", "PATCH"]) #Check
def alter_genero(id):
    genero = genero_name_web(**request.json)
    if valida_genero(**genero):
        update_genero(id, **genero)
        genero_cadastrado = get_genero(id)
        return jsonify(genero_name_db(genero_cadastrado))
    else:
        return jsonify({"erro": "Usuário inválido"})


@app.route("/generos/<int:id>", methods=["DELETE"]) #Not Working
def deletar_genero(id):
    try:
        delete_genero(id)
        return "", 204
    except:
        return jsonify({"erro": "Não foi possivel deletar"})


@app.route("/generos", methods=["GET"])
def buscar_genero():
    nome = nome_genero_from_web(**request.args)
    generos = select_genero(nome)
    generos_name_db = [genero_name_db(genero) for genero in generos]
    return jsonify(generos_name_db)


#########################################################################
######################################################################### CONTROLLER - DIRETORES
@app.route("/diretores", methods=["POST"]) #Check
def inserir_diretor():
    diretor = diretor_name_web(**request.json)
    if valida_diretor(**diretor):
        id_diretor = insert_diretor(**diretor)
        diretor_cadastrado = get_diretor(id_diretor)
        return jsonify(diretor_name_db(diretor_cadastrado))
    else:
        return jsonify({"erro": "Diretor inválido ou já inserido!"})


@app.route("/diretores/<int:id>", methods=["PUT", "PATCH"]) #Check
def alterar_diretor(id):
    diretor = diretor_name_web(**request.json)
    if valida_diretor(**diretor):
        update_diretor(id, **diretor)
        diretor_cadastrado = get_diretor(id)
        return jsonify(diretor_name_db(diretor_cadastrado))
    else:
        return jsonify({"Erro": "Usuário inválido"})


@app.route("/diretores/<int:id>", methods=["DELETE"]) #Check
def deletar_diretor(id):
    try:
        delete_diretor(id)
        return "", 204
    except:
        return jsonify({"Erro": "Diretor possui itens conectados a ele"})


@app.route("/diretores", methods=["GET"]) #Check
def buscar_diretor():
    nome_completo = nome_diretor_from_web(**request.args)
    diretores = select_diretor(nome_completo)
    diretores_name_db = [diretor_name_db(diretor) for diretor in diretores]
    return jsonify(diretores_name_db)


#########################################################################
######################################################################### CONTROLLER - FILMES
@app.route("/filmes", methods=["POST"]) #Check
def inserir_filme():
    filme = filme_name_web(**request.json)
    if valida_filme(**filme):
        id_filme = insert_filme(**filme)
        filme_cadastrado = get_filme(id_filme)
        return jsonify(filme_name_db(filme_cadastrado))
    else:
        return jsonify({"erro": "Filme inválido ou já cadastrado"})


@app.route("/filmes/<int:id>", methods=["PUT", "PATCH"]) #Check
def alterar_filme(id):
    filme = filme_name_web(**request.json)
    if valida_filme(**filme):
        update_filme(id, **filme)
        filme_cadastrado = get_filme(id)
        return jsonify(filme_name_db(filme_cadastrado))
    else:
        return jsonify({"Erro": "Filme inválido ou não existente!"})


@app.route("/filmes/<int:id>", methods=["DELETE"]) #Check
def deletar_filme(id):
    try:
        delete_fime(id)
        return "", 204
    except:
        return jsonify({"Erro": "Filme possui itens conectados a ele"})


@app.route("/filmes", methods=["GET"]) #Check
def buscar_filme():
    titulo = titulo_filme_from_web(**request.args)
    filmes = select_filme(titulo)
    filmes_name_db = [filme_name_db(filme) for filme in filmes]
    return jsonify(filmes_name_db)


#########################################################################
######################################################################### CONTROLLER - Usuários
@app.route("/usuarios", methods=["POST"])
def inserir_usuario():
    usuario = usuario_from_web(**request.json)  # 3 - formata o que vem da internet
    if valida_usuario(**usuario):
        id_usuario = insert_usuario(**usuario)
        usuario_cadastrado = get_usuario(id_usuario)
        return jsonify(usuario_from_db(usuario_cadastrado))
    else:
        return jsonify({"erro": "Usuário inválido"})


@app.route("/usuarios/<int:id>", methods=["PUT", "PATCH"])
def alterar_usuario(id):
    usuario = usuario_from_web(**request.json)  # 3 - formata o que vem da internet
    if valida_usuario(**usuario):
        update_usuario(id, **usuario)
        usuario_cadastrado = get_usuario(id)
        return jsonify(usuario_from_db(usuario_cadastrado))
    else:
        return jsonify({"erro": "Usuário inválido"})


@app.route("/usuarios/<int:id>", methods=["DELETE"])
def apagar_usuario(id):
    try:
        delete_usuario(id)
        return "", 204
    except:
        return jsonify({"erro": "Usuário possui itens conectados a ele"})


@app.route("/usuarios", methods=["GET"])
def buscar_usuario():
    nome_completo = nome_usuario_from_web(**request.args)
    usuarios = select_usuarios(nome_completo)
    usuarios_from_db = [usuario_from_db(usuario) for usuario in usuarios]
    return jsonify(usuarios_from_db)


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
