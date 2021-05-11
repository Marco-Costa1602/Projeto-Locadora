import random
import uuid

from flask import Flask, jsonify, request
from serializer import *
from validacao import valida_genero, valida_diretor, valida_filme, valida_usuario, valida_locacao, valida_pagamento
from models import *
from datetime import datetime, timedelta


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


#########################################################################
######################################################################### CONTROLLER - LOCAÇÕES
@app.route("/locacoes", methods=["POST"])
def fazer_locacao():
    locacao = locacao_from_web(**request.json['locacao'])
    pag_tipo = pagamento_from_web(**request.json['pagamento'])

    if valida_pagamento(**pag_tipo) and valida_locacao(**locacao):
        agora = datetime.now()
        fim = (agora + timedelta(hours=48))
        id_locacao = insert_locacao(agora, fim, **locacao)
        locacao_registrada = get_locacao(id_locacao)

        lista_status = ["aprovado", "em analise", "reprovado"]
        status = random.choice(lista_status)
        codigo_pagamento = str(uuid.uuid4())
        valor = get_filme(locacao["filmes_id"])["preco"]
        data_pg = datetime.now()
        locacoes_id = select_locacao_pag(locacao["usuarios_id"])["id"]
        id_pagamento = insert_pagamento(pag_tipo["tipo"], status, codigo_pagamento, valor, data_pg, locacoes_id)
        pagamento_registrado = get_pagamento(id_pagamento)

        return jsonify({"pagamento": pagamento_from_db(pagamento_registrado, data_pg), "locação": locacao_from_db(locacao_registrada, agora, fim)})
    else:
        return jsonify({"erro": "Falha na locação!"})


@app.route("/locacoes/user/<int:id>", methods=["GET"])
def check_locacao_user_id(id):
    return jsonify(query(f"Select * from locacoes inner join usuarios on usuarios.id = locacoes.usuarios_id AND usuarios_id = %s", [id,]))

@app.route("/locacoes/<int:id>", methods=["GET"])
def check_locacao_by_id(id):
    return jsonify(query(f"Select * from locacoes where locacoes.id = %s;", [id,]))

@app.route("/locacoes/filme/<int:id>", methods=["GET"])
def check_locacao_filme_id(id):
    return jsonify(query(f"""select locacoes.id as Locacao_id,
                         filmes.titulo as Titulo_do_filme,
                         usuarios.nome_completo as Nome_usuario,
                         data_inicio as Data_locacao, pagamento.status as Status_pagamento
                         from locacoes
                         inner join filmes on filmes.id = locacoes.filmes_id AND filmes_id = %s
                         inner join usuarios on usuarios.id = locacoes.usuarios_id
                         inner join pagamento on locacoes.id = pagamento.locacoes_id""", [id,]))

##############################################################################
##############################################################################



if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
