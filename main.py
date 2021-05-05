from mysql.connector import connect

CONFIGURACOES_BD = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "locadora",
}


def execute(sql, params=None):
    with connect(**CONFIGURACOES_BD) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            conn.commit()


def query(sql, params=None):
    with connect(**CONFIGURACOES_BD) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            return cursor.fetchall()


def insert(tabela, colunas, valores):
    execute(f"INSERT INTO {tabela} ({','.join(colunas)}) VALUES ({','.join(['%s' for x in valores])})", valores)
    print("Os valores foram inseridos com sucesso")


def delete(tabela, coluna, valor):
    execute(f"DELETE FROM {tabela} WHERE {coluna} = %s", (valor,))


def update(tabela, chave, valor_chave, colunas, vlr_coluna):
    sets = [f"{coluna} = %s" for coluna in colunas]
    execute(f"""Update {tabela} SET{",".join(sets)} WHERE {chave} = %s""", vlr_coluna + [valor_chave])


def select(tabela, chave=1, valor_chave=1, limit=100, offset=0):
    return query(f"""SELECT * FROM  {tabela} WHERE {chave} = %s  LIMIT {limit} offset {offset}""", (valor_chave,))


#query_holder = list((query("SELECT * FROM generos")))
#print(query_holder)