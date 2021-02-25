import pyodbc
import sys
sys.path.append("..")
from Entity.UsuarioModel import Usuario

server = "."
database = "EventSoftDB"
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes')
cursor = cnxn.cursor()

class UsuarioRepository():

    def Login(correo,contrasenia):
        sql = "SELECT * FROM USUARIO WHERE correo=? and contraseña=?"
        cursor.execute(sql,correo,contrasenia)
        usuarios = []
        for row in cursor.fetchall():
            usuario = Usuario(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4])
            usuarios.append(usuario)
            break
        return usuarios
    
    def Delete(id):
        try:
            sql = "DELETE FROM USUARIO WHERE id=?"
            cursor.execute(sql,id)
            cnxn.commit()
            return True
        except:
            cnxn.rollback()
            return False
    
    def Update(usuario):
        try:
            sql = "UPDATE USUARIO SET nombres = ?, apellidos= ?, correo=?, contraseña=? WHERE id = ?"
            cursor.execute(sql,usuario.nombres,usuario.apellidos,usuario.correo,usuario.contrasenia,usuario.id)
            cnxn.commit()
            return True
        except:
            cnxn.rollback()
            return False
        
    def Save(usuario):
        try:
            sql = "INSERT INTO USUARIO (nombres,apellidos,correo,contraseña) VALUES(?,?,?,?)"
            cursor.execute(sql,usuario.nombres,usuario.apellidos,usuario.correo,usuario.contrasenia)
            cnxn.commit()
            return True
        except:
            cnxn.rollback()
            return False
    
    def GetAll():
        sql = "SELECT * FROM USUARIO"
        cursor.execute(sql)
        usuarios = []
        for row in cursor.fetchall():
            usuario = Usuario(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4])
            usuarios.append(usuario)
        return usuarios


#obj = UsuarioRepository()
#result = obj.Login('max.lara@hotmail.com','4Rt56')
#print(result[0].nombres)
