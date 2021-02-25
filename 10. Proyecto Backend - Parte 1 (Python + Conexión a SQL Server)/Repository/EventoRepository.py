import pyodbc
import sys
sys.path.append("..")
from Entity.EventoModel import Evento

server = "."
database = "EventSoftDB"
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
cursor = cnxn.cursor()

class EventoRepository():
    def Delete(id):
        try:
            sql = "DELETE FROM EVENTO WHERE id=?"
            cursor.execute(sql,id)
            cnxn.commit()
            return True
        except:
            cnxn.rollback()
            return False
    
    def Update(evento):
        try:
            sql = "UPDATE EVENTO SET imagenUrl = ?, titulo= ?, descripcion=?, tiempo=? WHERE id = ?"
            cursor.execute(sql,evento.imagenUrl,evento.titulo,evento.descripcion,evento.tiempo,evento.id)
            cnxn.commit()
            return True
        except:
            cnxn.rollback()
            return False
        
    def Save(evento):
        try:
            sql = "INSERT INTO EVENTO (imagenUrl,titulo,descripcion,tiempo,usuarioId) VALUES(?,?,?,?,?)"
            cursor.execute(sql,evento.imagenUrl,evento.titulo,evento.descripcion,evento.tiempo,evento.usuarioId)
            cnxn.commit()
            return True
        except:
            cnxn.rollback()
            return False
    
    def GetAll():
        sql = "SELECT * FROM EVENTO"
        cursor.execute(sql)
        eventos = []
        for row in cursor.fetchall():
            evento = Evento(
                row[0],
                row[1],
                row[2],
                row[3],

                row[4],
                row[5])
            eventos.append(evento)
        return eventos

