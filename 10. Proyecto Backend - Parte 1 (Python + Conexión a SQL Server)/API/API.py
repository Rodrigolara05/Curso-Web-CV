from flask import Flask, jsonify, request
import sys
sys.path.append("..")
from Services.UsuarioService import UsuarioService
from Services.EventoService import EventoService

app = Flask(__name__)


@app.route('/', methods=['GET'])
def Home():
    return "<h1>LA API DE EVENT SOFT ESTA FUNCIONANDO</h1>"

#USUARIOS
@app.route('/usuarios', methods=['GET'])
def GetUsuarios():
    data = UsuarioService.GetAll()
    result = {"mensaje": "Se obtuvo todos los datos correctamente",
              "data": data,
              "code": 200}
    return jsonify(result)

#EVENTO
@app.route('/eventos', methods=['GET'])
def GetEventos():
    data = EventoService.GetAll()
    result = {"mensaje": "Se obtuvo todos los datos correctamente",
              "data": data,
              "code": 200}
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='7070', debug= False)
