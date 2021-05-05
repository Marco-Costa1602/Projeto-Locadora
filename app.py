from flask import Flask, jsonify, request
from main import query, execute
from serializer import genero_name_web, genero_name_db
from validacao import valida_genero
from models import insert_genero, get_genero, delete_genero, alter_genero


#Serializer serve para validação e formatação

app = Flask(__name__)

tabelas = ('filmes', 'generos', 'locacoes', 'pagamento', 'usuarios', 'diretores')


# Função para retornar as tabelas existentes no atual banco de dados.
@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return jsonify(query("SHOW TABLES"))
    elif request.method == "POST":
        return request.json


#########################################################################
######################################################################### CONTROLER - GÊNEROS
# Função para buscar dados nas tabelas.
@app.route("/generos", methods=["GET", "POST", "DELETE", "PATCH"])
def controller_genero():
    if request.method == "POST":
        genero = genero_name_web(**request.json)
        if valida_genero(**genero):
            insert_genero(**genero)
            genero_criado = get_genero(genero["nome"])
            return jsonify(genero_name_db(genero_criado))
        else:
            return jsonify({"Erro": "Genero inválido ou já inserido!"})

    if request.method == "GET":
        return jsonify(get_genero(**request.json))

    if request.method == "DELETE":
        delete_genero(**request.json)
        return jsonify(get_genero(**request.json))

    if request.method == "PATCH":
        alter_genero(request.json['atual'], request.json['novo'])
        return jsonify(get_genero(**request.json))


#########################################################################
######################################################################### CONTROLLER - DIRETORES
@app.route("/diretores", methods=["GET", "POST", "DELETE", "PATCH"])
def controller_diretores():
    if request.method == "GET":
        return jsonify(get)







########################################################################################## FETCH REGION
##########################################################################################
@app.route("/<string:rota>")
def fecth_others(rota):
    if rota in tabelas != "produtos":
        return jsonify(query(f"select * from {rota} limit 10"))


def price_str_convert(produto):
    return (produto[0], produto[1], produto[2], str(produto[3]))

@app.route("/produtos")
def fetch_produtos():
    produtos = [price_str_convert(produto) for produto in query("SELECT * FROM produtos")]
    return jsonify(produtos)
##########################################################################################
########################################################################################## FETCH REGION END



########################################################################################## ALTER REGION
##########################################################################################
@app.route("/alter/<string:rota>", methods=["GET", "PATCH"])
def alter_table(rota):
    rota = request.json["rota"]
    coluna = request.json["coluna"]
    cln_dado = request.json["dado"]
    vlr_local = request.json["valor_atual"]

    if rota in tabelas:
        modification = request.json["mod"]
        if modification == "A":

            execute(f"update {rota} set {coluna} = {cln_dado} where {coluna} = {vlr_local}")
            return jsonify(query(f"select * from {rota} where '{coluna}' = {cln_dado}"))
##########################################################################################
########################################################################################## ALTER REGION END



@app.route("/insert", methods=["GET", "POST"])
def insert():
    tabela = request.json["tabela"]
    valores = request.json["valores"]
    colunas = request.json["colunas"]
    vlr_holder = ['%s' for vlr in valores]
    concat_colunas = ', '.join(colunas)
    execute(f"INSERT INTO {tabela} ({concat_colunas}) VALUES ({', '.join(vlr_holder)})", valores)
    return jsonify(query("SELECT * FROM TB_PAIS WHERE ID = 240"))

##########################################################################################
##########################################################################################
#Select Specific




if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)

# jsonify({"metodo": request.method})

