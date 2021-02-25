from flask import Flask, jsonify, request
from flask_cors import CORS
from Services.UsuarioService import UsuarioService
from Services.EventoService import EventoService

app = Flask(__name__)
#cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
CORS(app)

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

@app.route('/usuario/login', methods=['POST'])
def Login():
    msg = ""
    code = 0
    data = UsuarioService.Login(request.json)
    if len(data)>0:
        msg = "Exito al iniciar sesion"
    else:
        msg = "Error al iniciar sesion"

    result = {
        "mensaje":msg,
        "data":data,
        "code": code
        }
    
    return jsonify(result)

@app.route('/usuario/save', methods=['POST'])
def SaveUsuario():
    msg = ""
    code = 0
    data = UsuarioService.Save(request.json)
    if data:
        msg = "Se registró al usuario correctamente"
    else:
        msg = "No se registró al usuario"

    result = {
        "mensaje" : msg,
        "data" : data,
        "code" : code
        }

    return jsonify(result)


#EVENTO
@app.route('/eventos', methods=['GET'])
def GetEventos():
    data = EventoService.GetAll()
    result = {"mensaje": "Se obtuvo todos los datos correctamente",
              "data": data,
              "code": 200}
    return jsonify(result)

@app.route('/evento/<int:id>', methods=['GET'])
def GetEvento(id):
    msg = ""
    code = 0
    data = EventoService.GetById(id)
    if len(data)>0:
        msg = "Se obtuvo el evento correctamente"
        code = 200
    else:
        msg = "No se encuentra el evento solicitado"
        code = 400
    result = {
        "mensaje": msg,
        "data": data,
        "code": code
        }
    
    return jsonify(result)

@app.route('/evento/usuario/<int:id>', methods=['GET'])
def GetEventoByUser(id):
    msg = ""
    code = 0
    data = EventoService.GetByUserId(id)
    if len(data)>0:
        msg = "Se obtuvo los eventos correctamente"
        code = 200
    else:
        msg = "No se encuentran los eventos solicitados"
        code = 400
    result = {
        "mensaje": msg,
        "data": data,
        "code": code
        }
    
    return jsonify(result)

@app.route('/evento/save', methods=['POST'])
def SaveEvento():
    msg = ""
    code = 0
    data = EventoService.Save(request.json)
    if data:
        msg = "Se registró el evento correctamente"
        code = 200
    else:
        msg = "No se registró el evento correctamente"
        code = 400

    result = {
        "mensaje" : msg,
        "data" : data,
        "code" : 200}
    
    return jsonify(result)

@app.route('/evento/update', methods=['PUT'])
def UpdateEvento():
    msg = ""
    code = 0
    data = EventoService.Update(request.json)
    if data:
        msg = "Se actualizó el evento satisfactoriamente"
        code = 200
    else:
        msg = "No se actualizó el evento"
        code = 400

    result = {
        "mensaje" : msg,
        "data" : data,
        "code" : 200
        }
    
    return jsonify(result)

@app.route('/evento/delete/<int:id>', methods=['DELETE'])
def DeleteEvento(id):
    msg = ""
    code = 0
    data = EventoService.Delete(id)
    if data:
        msg = "Se eliminó el evento satisfactoriamente"
        code = 200
    else:
        msg = "No se eliminó el evento"
        code = 400
    result = {
        "mensaje" : msg,
        "data" : data,
        "code" : code        
        }
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='7070', debug= False)
