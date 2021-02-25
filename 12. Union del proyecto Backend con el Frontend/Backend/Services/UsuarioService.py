from flask import jsonify,request
import json
import sys
sys.path.append("..")
from Entity.UsuarioModel import Usuario
from Repository.UsuarioRepository import UsuarioRepository

class UsuarioService():

    def Login(json):
        result = []
        try:
            usuarios = UsuarioRepository.Login(json['correo'],json['contrasenia'])
            if len(usuarios)>0:
                for item in usuarios:
                    result.append(item.toJson())
                    break
        except:
            print("Except")
            result = []
        print(result)
        return result
    
    def GetAll():
        result = []
        usuarios = UsuarioRepository.GetAll()
        for item in usuarios:
            result.append(item.toJson())
        return result

    def Save(json):
        result = False
        try:
            usuario = Usuario(
                json['id'],
                json['nombres'],
                json['apellidos'],
                json['correo'],
                json['contrasenia']
                )
            result = UsuarioRepository.Save(usuario)
        except:
            result = False
        return result



print("SE ESTA INVOCANDO A LA CLASE USUARIO SERVICE")
