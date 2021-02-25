from flask import jsonify,request
import json
import sys
sys.path.append("..")
from Entity.EventoModel import Evento
from Repository.EventoRepository import EventoRepository
#
class EventoService():

    def GetByUserId(id):
        result = []
        try:
            eventos = EventoRepository.GetByUserId(id)
            if len(eventos)>0:
                for item in eventos:
                    result.append(item.toJson())
        except:
            result = []
        return result

    def GetById(id):
        result = []
        try:
            eventos = EventoRepository.GetById(id)
            if len(eventos)>0:
                for item in eventos:
                    result.append(item.toJson())
                    break
        except:
            result = []
        return result
    
    def GetAll():
        result = []
        eventos = EventoRepository.GetAll()
        for item in eventos:
            result.append(item.toJson())
        return result
    
    def Save(json):
        result = False
        try:
            evento = Evento(
                json['id'],
                json['imagenUrl'],
                json['titulo'],
                json['descripcion'],
                json['tiempo'],
                json['usuarioId']
                )
            result = EventoRepository.Save(evento)
        except:
            result = False
        return result

    def Update(json):
        result = False
        try:
            evento = Evento(
                json['id'],
                json['imagenUrl'],
                json['titulo'],
                json['descripcion'],
                json['tiempo'],
                json['usuarioId']
                )
            result = EventoRepository.Update(evento)
        except:
            result = False
        return result

    def Delete(id):
        result = False
        try:
            result = EventoRepository.Delete(id)             
        except:
            result = False
        return result
        



print("SE ESTA INVOCANDO A LA CLASE EVENTO SERVICE")
