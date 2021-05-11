from datetime import datetime, timedelta
############################################################# Serializer - GENEROS
def genero_name_web(**kwargs):
    return {
        "nome": kwargs["nome"] if 'nome' in kwargs else ""
    }


def genero_name_db(genero):
    return{
        "id": genero["id"],
        "nome": genero["nome"],
    }

def nome_genero_from_web(**kwargs):
    return kwargs["nome"] if "nome" in kwargs else ""


def nome_genero_from_web(**kwargs):
    return kwargs["nome"] if "nome" in kwargs else ""


############################################################# Serializer - DIRETORES
def diretor_name_web(**kwargs):
    return{
        "nome_completo": kwargs if 'nome' in kwargs else ""
    }


def diretor_name_db(diretor):
    return{
        "id": diretor["id"],
        "nome_completo": diretor["nome_completo"],
    }


def nome_diretor_from_web(**kwargs):
    return kwargs["nome_completo"] if "nome_completo" in kwargs else ""


#############################################################
############################################################# Serializer - FILMES
def filme_name_web(**kwargs):
    return{
        "titulo": kwargs["titulo"] if 'titulo' in kwargs else "",
        "ano": kwargs["ano"] if 'ano' in kwargs else "",
        "classificacao": kwargs["classificacao"] if 'classificacao' in kwargs else "",
        "preco": kwargs["preco"] if 'preco' in kwargs else "",
        "diretores_id": kwargs["diretores_id"] if 'diretores_id' in kwargs else "",
        "generos_id": kwargs["generos_id"] if "generos_id" in kwargs else ""
    }


def filme_name_db(filme):
    return{
        "id": filme["id"],
        "titulo": filme["titulo"],
        "ano": filme["ano"],
        "classificacao": filme["classificacao"],
        "preco": str(filme["preco"]),
        "diretores_id": filme["diretores_id"],
        "generos_id": filme["generos_id"]
    }


def titulo_filme_from_web(**kwargs):
    return kwargs["titulo"] if "titulo" in kwargs else ""


#############################################################
############################################################# Serializer - USUÁRIOS
def usuario_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else "",
        "CPF": kwargs["CPF"] if "CPF" in kwargs else "",
    }


def usuario_from_db(usuario):
    return {
        "id": usuario["id"],
        "nome_completo": usuario["nome_completo"],
        "CPF": usuario["CPF"],
    }


def nome_usuario_from_web(**kwargs):
    return kwargs["nome_completo"] if "nome_completo" in kwargs else ""


#############################################################
############################################################# Serializer - LOCAÇÕES
def locacao_from_web(**kwargs):
    return{
        "filmes_id": kwargs["filmes_id"] if "filmes_id" in kwargs else "",
        "usuarios_id": kwargs["usuarios_id"] if "usuarios_id" in kwargs else "",
    }


def locacao_from_db(locacao, data_inicio, data_fim):
    return{
        "id": locacao["id"],
        "data_inicio": datetime.date(data_inicio).strftime("%d %B, %Y"),
        "data_fim": datetime.date(data_fim).strftime("%d %B, %Y"),
        "filmes_id": locacao["filmes_id"],
        "usuarios_id": locacao["usuarios_id"],
}


#############################################################
############################################################# Serializer - PAGAMENTOS
def pagamento_from_web(**kwargs):
    return{
        "tipo": kwargs["tipo_pagamento"] if "tipo_pagamento" in kwargs else "",
    }


def pagamento_from_db(pagamento, data_pg):
    return{
        "id": pagamento["id"],
        "tipo": pagamento["tipo"],
        "status": pagamento["status"],
        "codigo_pagamento": pagamento["codigo_pagamento"],
        "valor": str(pagamento["valor"]),
        "data": datetime.date(data_pg).strftime("%d %B, %Y"),
        "locacoes_id": pagamento["locacoes_id"]
    }
