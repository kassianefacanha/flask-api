from flask import Flask, request
from main import insertDados
app = Flask("Dados")

@app.route("/cadastra", methods=["POST"])
def cadastraDados():

    body = request.get_json()
    dados = insertDados(body["resolution"],body["issue_summary_id"], 
                            body["family_id"],body["system_id"], body["region_code"])

    return dados

app.run()