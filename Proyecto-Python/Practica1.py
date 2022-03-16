import ModuloExterno  #Libreria externa creada por mi
import random    #Libreria para utilizar operadores randomicos
import json #Libreria para utilizar objetos json
import pandas as pd  #Libreria para utilizar las tablas de pandas y hacer ETL (json -> pd ,  csv -> pd, etc)
import requests
from suds.client import Client

def ImprimirPantalla(flag, Valor1, Valor2):
    if flag:
        if Valor1:
            print("muchachos")
        else:
            print(Valor2)

#Debugger: Boton derecho de run para comenzar debugger en el breakpoint definido y F8 para avanzar linea a linea

#Prints
print("=========================")
print("Hola\na" +" "+"todos")
print("que")
print("tal")
print(123_456_789) #_ son comentarios para el compilador y sirven para mostrar numeros grandes al usuario
print(1.53) #Float
print(True) #Boolean
print(False) #Boolean

#Modulo externo creado por mi
print("======================")
print(f"Pi es: {ModuloExterno.pi}")
print("======================")

#Modulo
print("======================")
VariableX = 8 % 3
print("El modulo de 8 % 3 es: ")
print(VariableX)
print("======================")

#Randomico
print("======================")
print("El numero randomico es: ")
print(random.randint(3, 9))
print("======================")

#Casteos
print("=========================")
#STR A INT
NumeroStr = "123"
NumeroInt = int(NumeroStr) #Casteo de int
print(NumeroInt+4)

#STR A FLOAT
Numero2Str = "123.5"
Numero2Float = float(Numero2Str) #Casteo de float
print(Numero2Float+0.8)

#STR FORMATO FLOAT A INT
Numero3Str = "230.8"
Numero3Int = int(float(Numero3Str))
print(Numero3Int+5)

Variable = str(123)
Variable = str(158.5)
print("El resultado en str es: "+Variable);

#f-string
booleano = False
Entero = 5
Flotante = 2.3
print(f"El booleano es {booleano} , el entero es {Entero} , el Flotante es {2.3}.")

print("=========================")

#Verificar tipo de dato
print("Verificar tipos de datos")
print(type(2.5))
print(type(False))
print(type(5))

#Metodos float
print("=========================")
Variable = round(2.44343434)
Variable2 = round(2.44343434, 3)
print("Variable redondeada: "+str(Variable))
print("Variable redondeada con digitos: "+str(Variable2))
print("=========================")

#IF - ELSE IF - ELSE
Parametro = 3
Parametro2 = False
Parametro3 = True
print("=========================")
#Poner parentesis en las operaciones es opcional, no es obligatorio
#Operadores: and, or, not
if Parametro >= 1 and Parametro < 4:
    if (not Parametro2):
        if Parametro3:
            print("Parametro esta entre 1 y 4, incluyendo el 1, siendo Parametro2 True y Parametro3 True")
        else:
            print("Parametro esta entre 1 y 4, incluyendo el 1, siendo Parametro2 True y Parametro3 False")
    else:
        print("Parametro esta entre 1 y 4, incluyendo el 1, siendo Parametro2 False")
elif Parametro >= 4 and Parametro < 6:
    print("Parametro esta entre 4 y 6, incluyendo el 4")
else:
    print("Parametro es menor a 1 o igual o mayor a 6")
print("=========================")


#Metodos de string
print("=========================")
DatoStr = "Hola-mundo"
print(DatoStr.upper())
print(DatoStr.lower())
print(len(DatoStr))
print(DatoStr.split("-")[0])
print(DatoStr.split("-")[1])
print("=========================")

#Array
print("=========================")

Lista = ["Francisco", "Ignacio", "Kevin"]
print("Lista[0]: "+Lista[0])
print("=========================")

#While
print("=========================")
print("while")
i = 0
while i < len(Lista):
    print(Lista[i])
    i = i+1
print("=========================")

#do while no existe

#For
print("=========================")
print("for")

for val in Lista:
    print(val)

print("=========================")


print("=========================")

#Metodos Array
print("=========================")

Lista = ["Francisco", "Ignacio"]
print(len(Lista))
ModuloExterno.FuncionForLista(0,Lista,1)

Lista.append("Kevin") #Push
print(len(Lista))
ModuloExterno.FuncionForLista(0,Lista,1)

Lista.pop() #Pop
print(len(Lista))
ModuloExterno.FuncionForLista(0,Lista,1)
print("======")
Lista.append("Kevin") #Push
ModuloExterno.FuncionForLista(0,Lista,1)

print(f"Findindex: {Lista.index('Kevin')}") #FindIndex

#Contains
Lista.__contains__('a') #true / false

#FILTER
#=============================================
#Opcion = input("Seleccione un valor existente para filtrar: ")
Opcion = "a"

#Filter (Con function filtro
NuevaListaFilter = filter(lambda val: val != Opcion, Lista)

#Casteo objeto filter a array
NuevaListaArray = list(NuevaListaFilter)
print("Filter:")
ModuloExterno.FuncionForLista(0,NuevaListaArray,1)

print("=========================")


#Split.join
print("=========================")
VariableStr = "Hola-mundo-que-tal"
VariableArray = VariableStr.split("-")
VariableStr2 = "/".join(VariableArray)
print(f"VariableStr2: {VariableStr2}")
print("=========================")

#Split.pop
print("=========================")
VariableStr = "Hola-mundo-que-tal"
VariableMostrar = VariableStr.split("-").pop()
print(f"VariableMostrar: {VariableMostrar}")
print("=========================")



#Switch case no existe en python, para implementarla:
#Salir = False
Salir = True
while Salir == False:
    print("\n\n\n\n\n\n\nMenu")
    print("1.- Opcion 1")
    print("2.- Opcion 2")
    print("3.- Salir")
    Opcion = input("Elija una opcion: ")
    if Opcion == "1":
        print("Opcion 1")
    elif Opcion == "2":
        print("Opcion 2")
    elif Opcion == "3":
        print("Salir")
        Salir = True
    else:
        print("Opcion no reconocida")




#Funcion
print("=========================")
ImprimirPantalla(True, False, "Hola");
print("=========================")

#Funcion Lambda (Arrow function de javascript en python)
print("=========================")
print("Funcion lambda")
Incrementar = lambda x: x+1
print(Incrementar(5))

MultiplicacionFunc = lambda x,y: x*y*3
print(MultiplicacionFunc(5,10))
print("=========================")

#Scope = Nivel de acceso. Las variables globales tienen un scope y las funciones tienen otro scope.
print("=========================")
VariableGlobal = 5

def FuncionScopeLocal():
    global VariableGlobal #Con la etiqueta global puedo llamar a funciones globales dentro de un scope local
    print(VariableGlobal)
    VariableGlobal += 1

FuncionScopeLocal()
print(VariableGlobal)
print("=========================")


#Input
#Dato = input("Inserte su dato: ")
Dato = "A"
print("El dato insertado fue: "+Dato)


#Obtencion de data
#===============================

#CSV
print("=========================")
#FILE
#=========
#URL:
#URLCSV = "https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2020-financial-year-provisional/Download-data/annual-enterprise-survey-2020-financial-year-provisional-csv.csv"

#PATH:
#PathCSV = "./csv_input.csv"
#df = pd.read_csv(PathCSV)
#print(df)
print("=========================")

#JSON
print("=========================")

#PATH
#======
#with open("./json_input.json") as json_file:
#    JsonArray = json.load(json_file) #parse

#print("JsonArray: " + json.dumps(JsonArray)) #stringify

#STRING
#=======
#JsonString = '[{"Nombre": "Francisco", "Edad": 27}, {"Nombre": "Kevin", "Edad": 24}, {"Nombre": "Ignacio", "Edad": 27}]'
#JsonArray = json.loads(JsonString)  #Loads = JSON.parse
#print("JsonArray: "+json.dumps(JsonArray)) #Dumps = JSON.stringify

#URL (API REST)
#================
#JsonURL = "https://pokeapi.co/api/v2"
#response = requests.get(JsonURL)

#if response.status_code == 200:
#    JsonObj = json.loads(response.content)
#    print("El json es: "+json.dumps(JsonObj))
#else:
#    print("La URL es erronea")


#Enviar JSON de File a PD
#JsonPath = "./json_input.json"
#df = pd.read_json(JsonPath)
#print(df)

#Enviar JSON de String a PD
#JsonString = [{"Nombre": "Francisco", "Edad": 27}, {"Nombre": "Kevin", "Edad": 24}, {"Nombre": "Ignacio", "Edad": 27}]
#df = pd.DataFrame(JsonString)
#print(df)

print("=========================")


#I/O
#=======================

#IN
with open('input.txt') as file:
    lines = file.read()

print(lines)

#OUT
with open('input.txt', 'w') as file:
    file.write("abc")


#IN & OUT
with open('./input.txt', 'r') as file_reader, open('./output.txt', 'w') as file_writer:
    lines = file_reader.read()
    file_writer.write(lines)




#POO
#---------
print("===================================")
class Clase:
    def __init__(self, id, rut, nombre):
        self.id = id
        self.rut = rut
        self.nombre = nombre

    def getId(self):      #En python puedo obtener las ids mediante .id o un metodo get
        return self.id

    def updateClase(self, rut, nombre):
        self.rut = rut
        self.nombre = nombre

ArregloClases = []
i = 0
"""
while i < 3:
    rut = input("Ingrese rut: ")
    nombre = input("Ingrese nombre: ")

    obj = Clase(i+1, rut, nombre)
    ArregloClases.append(obj)
    i += 1

RutSelector = input("Ingrese rut a actualizar: ")
NuevoRut = input("Ingrese nuevo rut: ")
NuevoNombre = input("Ingrese nuevo nombre: ")

flag = False
i = 0
while i < len(ArregloClases):
    if RutSelector == ArregloClases[i].rut :
        ArregloClases[i].updateClase(NuevoRut, NuevoNombre)
        print(f"El nuevo nombre para el rut {ArregloClases[i].rut} es: {ArregloClases[i].nombre}")
        flag = True
        break
    i += 1

if flag == False:
    print("No hubo rut que coincidiera con alguno de los ingresados")
"""
print("====================================")


#SOAP Webservices (Con suds)
"""
operation = Client("http://localhost:8000/?wsdl")
prueba = getattr(operation.service, "prueba")
print(prueba("Francisco"))
print(operation.service.prueba("Francisco"))
"""

