from flask import Flask, request

app = Flask("Youtube")

@app.route("/olamundo", methods=["GET"])
def olaMundo():
    return{"Olá" :"Mundo"}
    
@app.route("/cadastra/usuario", methods=["POST"])
def cadastraUsuario():

    body = request.get_json()
    print(body)

    return body

app.run()