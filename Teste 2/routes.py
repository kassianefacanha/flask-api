from flask import Flask, request
from main import insertDados
app = Flask("Dados")


@app.route("/")
def hello_world():
  return "Hello, World!"

  
@app.route("/resolution_templateG", methods=["GET"])
def root():
    return{"resolution": "string",
  "issue_summary_id": 0,
  "family_id": 0,
  "system_id": 0,
  "region_code": 0}


@app.route("/resolution_template", methods=["POST"])
def cadastraDados():

    body = request.get_json()
    dados = insertDados(body["resolution"],body["issue_summary_id"], 
                            body["family_id"],body["system_id"], body["region_code"])

    return dados

app.run()