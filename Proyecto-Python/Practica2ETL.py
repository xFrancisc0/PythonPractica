import random
import numpy as np
import pandas as pd

#Referencia: https://www.youtube.com/watch?v=8ASjvOIyyl8&t=274s&ab_channel=LeonardoKuffo

PathCSV = "./weather_data.csv"
df = pd.read_csv(PathCSV, index_col="id")

#Descubrir data
#=============
df_primeras = df.head(2) #Primeras dos
df_ultimas = df.tail(2) #Ultimas dos
df_estadisticadescriptiva = df.describe()


#Limpiar data
#==============
df_eliminarfilasconNan = df.dropna()
#df_reemplazardataNan = df.fillna(0) Para todas las filas los nan es 0
df_reemplazardataNan = df.fillna({"temp": 0, "data2": -1})

#Filtrar data por columnas
#==========================
df_filtrado = df["temp"]
df_filtrado = df[["temp", "data2"]]

#Filtrar data por filas
#==========================
df_filtrado = df.iloc[[0,2]] #Mostrar solo fila con posicion 0 y 3 del array de pandas
df_filtrado = df.iloc[1:3] #Mostrar filas desde la posicion 1 a la 3
df_filtrado = df.loc[2:4] #Idem, este sirve para trabajar con ids de la data en si misma y no del array
df_filtrado = df.loc[[1,3]] #Idem, este sirve para trabajar con ids de la data en si misma y no del array

#Filtrar data por filas y columnas
#==========================
df_filtrado = df.loc[[1,3] , ["temp", "data2"]]  #Filtro al inicio por filas dada las ids reales y por columnas


#Filtrar data por condiciones
#==========================
nuevo_df = df.fillna(0)
df_filtrado = df.fillna(0)[((df.fillna(0)["temp"] > 14) & (df.fillna(0)["data2"] < 9)) | (df.fillna(0)["temp"] == 0)] #Filtrar por numeros

df_filtrado = df[df["day"].str.contains("Monday")] #Filtrar por texto


#Agregar columnas nuevas transformadas
print("======================================")
#df[output] = df[input].apply(funcion)

##1 VARIABLE

#Con funciones lambda
nuevo_df = df.fillna(0)
nuevo_df["TemperaturaFuncion"] = nuevo_df["temp"].apply(lambda temp: temp*3)

#Con funciones
def Funcion(temp):
    return temp*3

nuevo_df = df.fillna(0)
nuevo_df["TemperaturaFuncion"] = nuevo_df["temp"].apply(Funcion)


##MULTIPLES VARIABLES = LE MANDO LA FILA COMPLETA

def Funcion(Fila):
    return Fila["temp"] * Fila["data2"]

nuevo_df = df.fillna(0)
nuevo_df["TemperaturaFuncion"] = nuevo_df.apply(Funcion, axis=1)
print("======================================")



#AGRUPACION DE DATA
#La data se agrupa por un campo comun (Ejemplo: categoria, pais, region, ciudad)
#Y luego se calcula una medida estadistica por campo, por ejemplo la media o el maximo
print("======================================")

df_agrupado = df.groupby("categoria")\
                .agg({
                    "temp":"mean",
                    "data2":"max"
                })

print(df_agrupado)
print("======================================")

