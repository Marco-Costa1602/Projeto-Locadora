############################################################# Serializer - GENEROS
def genero_name_web(**kwargs):
    return {
        "nome": kwargs["nome"] if 'nome' in kwargs else ""
    }


def genero_name_db(*args):
    return{
        "nome": args[0]
    }


############################################################# Serializer - DIRETORES
def diretor_name_web(**kwargs):
    return{
        "nome_completo": kwargs["nome_completo"] if 'nome_completo' in kwargs else ""
    }


def diretor_name_db(*args):
    return{
        "nome_completo": args[0]
    }
############################################################# Serializer -
