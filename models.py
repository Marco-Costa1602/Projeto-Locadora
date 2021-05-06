from main import insert, delete, update, query




############################################################################## Funções - Gênero
##############################################################################

list_holder = query("SELECT * FROM generos")


def insert_genero(nome):
    insert('generos', ('nome',), (nome,))


def update_genero(nome, novo):
    update('generos', 'nome', nome, ('nome',), (novo,))


def get_genero(nome):
    return query(f"SELECT * FROM generos WHERE nome LIKE %s", (nome,))


def delete_genero(nome):
    delete("generos", "nome", nome)
    query("SELECT * FROM generos")


##############################################################################
############################################################################## Funções - Diretor

def get_diretor(nome_completo):
    return query(f"SELECT * FROM diretores WHERE nome_completo LIKE %s", (nome_completo,))


def insert_diretor(nome_completo):
    insert('diretores', ('nome_completo',), (nome_completo,))


def delete_diretor(nome_completo):
    delete("diretores", "nome_completo", nome_completo)
    query("SELECT * FROM diretores")

def update_diretor(nome_completo, novo):
    update('diretores', 'nome_completo', nome_completo, ('nome_completo',), (novo,))


