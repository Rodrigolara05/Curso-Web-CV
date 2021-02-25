import json
class Usuario():
    id: int
    nombres: str
    apellidos: str
    email: str
    contrasenia: str

    def __init__(self,id,nombres,apellidos,correo,contrasenia):
        self.id = id
        self.nombres = nombres
        self.apellidos=apellidos
        self.correo=correo
        self.contrasenia=contrasenia

    def toJson(self):
        return json.dumps(self.__dict__)
