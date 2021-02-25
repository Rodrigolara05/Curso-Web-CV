import json
class MovieModel():
    id: int
    name: str
    director: str
    costo: float
    moneda: str
    annio: str
    def __init__(self,id,name,director,costo,moneda,annio):
        self.id = id
        self.name = name
        self.director = director
        self.costo = costo
        self.moneda = moneda
        self.annio = annio
    def toJson(self):
        return json.dumps(self.__dict__)
        
print("SE ESTA INVOCANDO A LA CLASE MOVIE")
