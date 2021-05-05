from main import insert, delete, update, query




############################################################################## Funções - Gênero
##############################################################################

list_holder = query("SELECT * FROM generos")


def insert_genero(nome):
    insert('generos', ('nome',), (nome,))


def alter_genero(atual, novo):
    update('generos', 'nome', atual, 'nome', novo)


def get_genero(nome):
    return query("SELECT * FROM generos")


def delete_genero(nome):
    delete("generos", "nome", nome)
    query("SELECT * FROM generos")


##############################################################################
############################################################################## Funções - Diretor

def get_diretor(nome):
    return query("SELECT * FROM diretores")


def insert_diretor(nome):
    insert('diretores', 'nome_completo', nome)