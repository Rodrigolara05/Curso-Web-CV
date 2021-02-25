from flask import jsonify,request
import json
import sys
sys.path.append("..")
from Entity.UsuarioModel import Usuario
from Repository.UsuarioRepository import UsuarioRepository

class UsuarioService():
    
    def GetAll():
        result = []
        usuarios = UsuarioRepository.GetAll()
        for item in usuarios:
            result.append(item.toJson())
        return result


print("SE ESTA INVOCANDO A LA CLASE USUARIO SERVICE")
