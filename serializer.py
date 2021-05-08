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
