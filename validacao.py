from models import get_genero
from main import select, query


def valida_genero(nome):
    list_holder = [item['nome'] for item in query("SELECT nome FROM generos")]
    if nome in list_holder:
        return False
    if len(nome) == 0:
        return False
    elif len(nome) > 255:
        return False
    return True


def valida_diretor(nome_completo):
    list_holder = [item['nome_completo'] for item in query("SELECT nome_completo FROM diretores")]
    if nome_completo in list_holder:
        return False
    if len(nome_completo) == 0:
        return False
    elif len(nome_completo) > 255:
        return False
    return True


def valida_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    diretor_id_holder = [item['id'] for item in query("SELECT id FROM diretores")]
    genero_id_holder = [item['id'] for item in query("SELECT id FROM generos")]
    title_holder = [item['titulo'] for item in query("SELECT titulo FROM filmes")]

    if len(titulo) == 0 or titulo in title_holder or len(titulo) > 255:
        return False

    elif ano < 1950 or ano > 2021:
        return False

    elif preco <= 0:
        return False

    elif diretores_id not in diretor_id_holder:
        return False

    elif generos_id not in genero_id_holder:
        return False

    return True


def valida_usuario(nome_completo, CPF):
    if len(nome_completo) == 0:
        return False

    if len(CPF) != 14:
        return False

    return True
