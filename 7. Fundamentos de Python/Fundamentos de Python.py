#Fundametos de Python
#C++
# private int numero = 0;
#cout

#JS
# var,let,const numero = 0;
# console.log("numero es:" + numero)

#Python
nombre = "Rodrigo"
VoF = True
#double o float o decimal es con el "."
altura = 1.75

n,n2, n3 = 5,4,7
numero_complejo = 2.1 + 7.8j

""" Tipo de datos"""
tipo_variable = type(n)
print("La variable con valor " + str(n) + " es de tipo: " + str(tipo_variable))
tipo_variable = type(nombre)
print("La variable con valor " +str(nombre) + " es de tipo: " + str(tipo_variable))
tipo_variable = type(numero_complejo)
print("La variable con valor " +str(numero_complejo) + " es de tipo: " + str(tipo_variable))


#Simbolos

suma = n2 + n3
print("Suma: " + str(suma))
resta = n2 - n3
print("Resta: " + str(resta))
multi = n2*n3
print("Multiplicación: " + str(multi))
divi = n2/n3
print("Division: " + str(divi))
potencia = 10 ** 4
print("Potencia: " + str(potencia))
division_entera = 100 // 3
print("Division Entera: " + str(division_entera))
residuo = 24 % 7
print("Residuo: " + str(residuo))
incremento_de_dos = 10
incremento_de_dos += 5
print(str(incremento_de_dos))
decremento_de_cinco = 10
decremento_de_cinco -= 5
print(str(decremento_de_cinco))


#Condicionales

print("Software Base")
variable = input("Ingrese un numero positivo: ")
number = int(variable)

if number < 0:
    print("El numero no es positivo")
else:
    print("El numero es positivo")


variable = input("Ingrese una edad: ")
edad = int(variable)
if edad > 17 :
    print("Es mayor de edad")
elif edad < 0:
    print("Edad no es valida")
else:
    print("Es menor de edad")


variable = input("Ingrese una edad para entrar a los juegos mecanicos: ")
edad = int(variable)

if edad>17 and edad <60: #&&
    print("Esta apto")
else:
    print("No esta apto")



variable = input("Ingrese su codigo de admin: ")
codigo = int(variable)

if codigo == 1 or codigo == 2: #||
    print("Tiene acceso")
else:
    print("No tiene acceso")

#Arrays


lista = ['pera','papaya','lucuma','palta']
print(lista)

#Añado un elemento a la lista
lista.append('limon')
print(lista)

#Añadir en posicion
lista.insert(1,'uva')
print(lista)

#Añadir una lista a la lista
lista2 = ['fresa', 'toronja', 'lechuga']
lista.extend(lista2)
print(lista)

#Eliminar por valor o dato
lista.remove('toronja')
print(lista)

#Eliminar por posición
lista.pop(1)
print(lista)

#Segunda manera de eliminar por posición
del lista[5]
print(lista)

#Eliminar ultimo elemento de la lista
lista.pop()
print(lista)

#Contar repeticion de un valor en la lista
veces = lista.count('pera')
print('Veces que se repite palta :' + str(veces))

#Encontrar la posicion de la primera coincidencia
posicion = lista.index('lucuma')
print("Indice de la primera coincidencia al buscar Lucuma: " + str(posicion))

#Revertir el orden
lista.reverse()
print(lista)

#Ordenamiento ascendente
lista.sort()
print(lista)

#ordenamiento de manera descendente
lista.sort(reverse=True)
print(lista)


#Eliminar todos los datos
lista.clear()
print(lista)


#Matriz, Tuplas

matriz = [
    [1,2,[2,3],4],
    [1,2,3,4,5,6],
    [1,2],
    ['Rodrigo']
    ]

print(matriz)

#tupla = (10,30)
#print(str(type(tupla)))

matriz_de_tupla = [
    (40,80),
    (4,10),
    (21,70)
    ]

print(matriz_de_tupla)
print(" ----------------- ")

#Bucles, Ciclos, Repetitivas

#Bucle FOR

for elemento in lista:
    print(elemento)

for number in range(2,6): ##Secuancia incrementa cada 1
    print(number)

for number in range(2,6,3): ##Secuancia incrementa cada 3
    print(number)
else:
    print("Termino!")

for elemento in range(len(lista)):
    print(elemento)

for elemento in matriz:
    print(elemento)
    for j in elemento:
        print(j)
    
for (edad,peso) in matriz_de_tupla:
    print("La edad es : " + str(edad))
    print("Y el peso es : " + str(peso))
    

#Bucle While:
a,b = 0,5
while a < b:
    print(a)
    a += 5


#Funciones

#Funcion simple
def imprimir_hola_mundo():
    print('Hola mundo!')


imprimir_hola_mundo()

#Funciones con paramteros
def imprimir_msg_bienvenida(nombre,apellido):
    print('Hola {} {}'.format(nombre,apellido))


imprimir_msg_bienvenida('Liliana','Yanqui')

#Palabras clave como parametros

def imprimir_msg_general(str):
    print(str)
    return;

imprimir_msg_general(str = 'Mi cadena')


def imprimir_invitacion_cumpleaños(direccion, nombre):
    print('Hola {} estas invitado a mi fiesta que se envunetra en {}. Te espero!'.format(nombre,direccion))



imprimir_invitacion_cumpleaños(nombre = 'Max', direccion = 'Av. Los proceres 123')


#Parametros con valores por defecto
def imprimir_informacion(name, edad = 0):
    print('Nombre : ' + name)
    if edad != 0:
        print('Edad : ' + str(edad))

imprimir_informacion('Pedro')



#Manipulacion de cadenas

palabra = "Hola Mundo"

#Concatenacion
print(palabra + "!")

#Multiplicacion
print(palabra * 3)

#Tamaño de la palabra
print(len(palabra))

#Recorrer la cadena
for l in palabra:
    print(l)

#Acceder a posiciones
print(palabra[3])

#Obtener un segmento de cadena
print(palabra[5:])

#Formateo
print("¡ {} !".format(palabra))

#Metodos
    #Mayusculas
print(palabra.upper())
    #Minuscula
print(palabra.lower())
    #Confirmaciones
print(palabra.isupper())
print(palabra.islower())

print(palabra.startswith('Hola'))
print(palabra.endswith('o'))

#Metodos join() y split()
mi_lista = ['gato','perro','loro']
texto_unido = "-".join(mi_lista)
print(texto_unido)

texto_final = "SmartFitABCBodytechABCGoldGym"
gym_lista = texto_final.split('ABC')
print(gym_lista)


#Diccionarios


#Definicion
diccionario = {
    'frio' : 'cold',
    'caliente' : 'hot'
    }
print(diccionario)

#Acceder a un valor por clave
print(diccionario['caliente'])

#Metodos para recorrer diccionario: keys(), values() y items()
print("\nMetodos para recorrer diccionario :")
print("Por llaves :")
for k in diccionario.keys():
    print(k)

print("Por Valor :")
for v in diccionario.values():
    print(v)

print("Por Item :")
for i in diccionario.items():
    print(i)

#Comprobar si el valor existe en una clave, valor o item

print('frio' in diccionario.keys())
print('hot' in diccionario.values())
print('caliente' in diccionario)

#Metodo GET
print(diccionario.get('caliente'))

#Añadir datos
diccionario.setdefault('Llave', 'Valor')
print(diccionario)



#Clases

class Evento():
    id = None
    titulo = None
    descripcion = None
    imagenURL = None

    def __init__(self, titulo):
        self.titulo = titulo
        print("Este es el constructor")

    def setTitulo(self, value):
        self.titulo = value
        
    def setDescripcion(self, value):
        self.descripcion = value

    def getId(self):
        return self.id

    def printInformation(self):
        print(self.titulo)
        print(self.descripcion)

evento = Evento('Musica Electro')
print(evento.titulo)
evento.setDescripcion('Esta es la descripcion')
print(evento.descripcion)
print(evento.getId())



class ClaseHija(Evento): #definicion de la clase hija
    def __init__(self):
        print("Se inicio el constructor de la clase hija")


claseH = ClaseHija()
print(claseH.getId())
claseH.setTitulo('Titulo 2')
claseH.setDescripcion('Esta es la descripcion 2')
claseH.printInformation()


def getInformation():
    try:
        print(10/0)
    except ZeroDivisionError:
        print("OPS! No se puede dividr entre 0")
        print(ZeroDivisionError)
    finally:
        print("La funcion se termino")

getInformation()
