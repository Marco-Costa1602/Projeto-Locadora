from models import get_genero
from main import select, query


def valida_genero(nome):
    list_holder = [item[0] for item in query("SELECT nome FROM generos")]
    if nome in list_holder:
        return False
    if len(nome) == 0:
        return False
    elif len(nome) > 255:
        return False
    return True


def valida_diretor(nome):
    list_holder = [item[0] for item in query("SELECT nome_completo FROM diretores")]
    if nome in list_holder:
        return False
    if len(nome) == 0:
        return False
    elif len(nome) > 255:
        return False
    return True