from flask import jsonify,request
import json
import sys
sys.path.append("..")
from Entity.EventoModel import Evento
from Repository.EventoRepository import EventoRepository

class EventoService():
    
    def GetAll():
        result = []
        eventos = EventoRepository.GetAll()
        for item in eventos:
            result.append(item.toJson())
        return result


print("SE ESTA INVOCANDO A LA CLASE EVENTO SERVICE")
