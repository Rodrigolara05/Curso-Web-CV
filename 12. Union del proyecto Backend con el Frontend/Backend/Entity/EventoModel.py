import json
class Evento():
    id: int
    imagenUrl: str
    titulo: str
    descripcion: str
    tiempo: str
    usuarioId: int

    def __init__(self,id,imagenUrl,titulo,descripcion,tiempo,usuarioId):
        self.id = id
        self.imagenUrl = imagenUrl
        self.titulo=titulo
        self.descripcion=descripcion
        self.tiempo=tiempo
        self.usuarioId=usuarioId

    def toJson(self):
        return json.dumps(self.__dict__)
