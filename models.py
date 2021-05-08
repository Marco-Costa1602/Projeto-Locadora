from main import insert, delete, update, query, select, select_like



############################################################################## Funções - Gênero
##############################################################################

list_holder = query("SELECT * FROM generos")


def insert_genero(nome):
    return insert('generos', ('nome',), (nome,))


def update_genero(id_atual, nome):
    update('generos', 'id', id_atual, ('nome',), [nome,])


def get_genero(id_genero):
    return select("generos", "id", id_genero)[0]


def select_genero(nome):
    return select_like("generos", "nome", nome)


def delete_genero(id_genero):
    delete("generos", "id", id_genero)


##############################################################################
############################################################################## Funções - Diretor

def get_diretor(id_diretor):
    return select("diretores", "id", id_diretor)[0]


def insert_diretor(nome_completo):
    return insert('diretores', ('nome_completo',), (nome_completo,))


def select_diretor(nome_completo):
    return select_like("diretores", "nome_completo", nome_completo)


def delete_diretor(id_diretor):
    delete("diretores", "id", id_diretor)


def update_diretor(id_diretor, nome_completo):
    update('diretores', 'id', id_diretor, ('nome_completo',), [nome_completo,])


##############################################################################
############################################################################## Funções - FILMES

def get_filme(id_filme):
    return select("filmes", "id", id_filme)[0]


def insert_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    return insert('filmes', ('titulo', 'ano', 'classificacao', 'preco', 'diretores_id', 'generos_id'), (titulo, ano, classificacao, preco, diretores_id, generos_id))


def update_filme(id_filme, titulo, ano, classificacao, preco, diretores_id, generos_id):
    update("filmes", "id", id_filme, ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"], [titulo, ano, classificacao, preco, diretores_id, generos_id])


def delete_fime(id_filme):
    delete("filmes", "id", id_filme)


def select_filme(titulo):
    return select_like("filmes", "titulo", titulo)


##############################################################################
############################################################################## Funções - FILMES
def insert_usuario(nome_completo, CPF):
    return insert("usuarios", ["nome_completo", "CPF"], [nome_completo, CPF])


def get_usuario(id_usuario):
    return select("usuarios", "id", id_usuario)[0]


def update_usuario(id_usuario, nome_completo, CPF):
    update("usuarios", "id", id_usuario, ["nome_completo", "CPF"], [nome_completo, CPF])


def delete_usuario(id_usuario):
    delete("usuarios", "id", id_usuario)


def select_usuarios(nome_completo):
    return select_like("usuarios", "nome_completo", nome_completo)
