from flask import Flask, jsonify, request
import sys
sys.path.append("..")
from Services.MovieServices import MovieService

app = Flask(__name__)

@app.route('/', methods=['GET'])
def Home():
    return "<h1>LA API ESTA FUNCIONANDO</h1>"

@app.route('/movies', methods=['GET'])
def GetMovies():
    data = MovieService.GetAll()
    result = {"mensaje": "Se obtuvo todos los datos correctamente",
              "movies": data,
              "code": 200}
    return jsonify(result)

@app.route('/movies', methods=['POST'])
def SaveMovie():
    result = MovieService.Save(request.json)
    result = {"mensaje": "Se grabó el dato correctamente",
              "result": result,
              "code": 200}
    return jsonify(result)

@app.route('/movies', methods=['PUT'])
def UpdateMovie():
    result = MovieService.Update(request.json)
    result = {"mensaje": "Se actualizo el dato correctamente",
              "result": result,
              "code": 200}
    return jsonify(result)

@app.route('/movies/<int:id>', methods=['DELETE'])
def DeleteMovie(id):
    result = MovieService.DeleteById(id)
    result = {"mensaje": "Se eliminó el dato correctamente",
              "result": result,
              "code": 200}
    return jsonify(result)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port='7070', debug= False)
