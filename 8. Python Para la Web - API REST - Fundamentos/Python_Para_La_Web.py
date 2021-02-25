from flask import Flask, jsonify, request
app = Flask(__name__)

cursos = [
    {"id" : 1,"nombre" : "Programación con Angular","precio" : 100,"cantidad" : 3},
    {"id" : 2,"nombre" : "Programación con React","precio" : 800,"cantidad" : 10},
    {"id" : 3,"nombre" : "Programación con Flutter","precio" : 600,"cantidad" : 5},
    {"id" : 4,"nombre" : "Programación con Python","precio" : 900,"cantidad" : 2}
    ]

@app.route('/', methods=['GET'])
def home():
    return 'El API está funcionando'

@app.route('/saludo/<name>', methods =['GET'])
def saludo(name):
    return 'Hola ' + name + ' tu API está funcionando!'

@app.route('/cursos', methods = ['GET'])
def GetCursos():
    if len(cursos) == 0:
        return jsonify({"cursos" : cursos, "code": 200, "mensaje" : "No hay ningun curso para mostrar"})
    return jsonify({"cursos" : cursos, "code": 200, "mensaje" : "Los datos se retornaron satisfactoriamente"})

@app.route('/cursos/<int:id>', methods = ['GET'])
def GetCursoById(id):
    result = None
    for curso in cursos:
        if curso['id'] == id:
            result = curso
            break
    if (result == None):
        return jsonify({"error" : "Curso no encontrado","curso": result})
    return jsonify({"curso" : result, "code":200})

@app.route('/cursos', methods = ['POST'])
def AddCurso():
    nuevoCurso = {"id" : request.json['id'],
                  "nombre" : request.json['nombre'],
                  "precio" : request.json['precio'],
                  "cantidad" : request.json['cantidad']}
    cursos.append(nuevoCurso)
    return jsonify({"cursos" : cursos, "code": 200, "mensaje" : "Los datos se retornaron satisfactoriamente"})

@app.route('/cursos/<int:id>', methods = ['DELETE'])
def DeleteById(id):
    result = None
    for curso in cursos:
        if curso['id'] == id:
            result = curso
            break
    if result == None:
        return jsonify({"error":"Curso no encontrado"})
    cursos.remove(result)
    return jsonify({"cursos" : cursos,"mensaje" : "El registro fue eliminado satistactoriamente"})

@app.route('/cursos', methods = ['DELETE'])
def DeleteAll():
    cursos.clear()
    return jsonify({"cursos" : cursos,"mensaje" : "Todos los registros fueron eliminados"})

@app.route('/cursos', methods = ['PUT'])
def UpdateCurso():
    try:
        id = request.json['id']
        result = None
        for curso in cursos:
            if curso['id'] == id:
                result = curso
                break
        if result != None:
            nuevoCurso = {"id" : request.json['id'],
                      "nombre" : request.json['nombre'],
                      "precio" : request.json['precio'],
                      "cantidad" : request.json['cantidad']}
            result['nombre'] =  nuevoCurso['nombre']
            result['precio'] =  nuevoCurso['precio']
            result['cantidad'] =  nuevoCurso['cantidad']        
            return jsonify({"mensaje" : "Curso actualizado","curso": nuevoCurso})
        else:
            return jsonify({"error" : "Curso no encontrado","curso": result})
    except:
        return jsonify({"error" : "Algo fue mal, verifique sus datos e intentelo nuevamente"})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port='1213',debug = False)


































