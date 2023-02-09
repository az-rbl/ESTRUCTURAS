# Asignacion_2.py
# Implementación de algoritmo de Burbuja
#Esta asignación consiste en agregar al código lo siguiente:
#Implementar el algoritmo de ordenamiento  de  Burbuja.
#La función debe recibir com parámetro de entrada el arreglo o lista a ordenar. 
#Badillo Lora Raúl

#Modulo que contiene la funcion para generar una lista con valores aleatorios
import Asignacion_1 as r
from datetime import datetime

#Regrsa una lista ordenada por el algoritmo burbuja, recibe una lista
def burbuja(lista):
    for x in range(len(lista)-2):
        for y in range(len(lista)-1,-1,-1):
            if y ==x:
                break
            if lista[y]< lista[y-1]:
                temp, lista[y] = lista[y], lista[y-1]
                lista[y-1] = temp
    return lista
        
        
if __name__=="__main__":
    l=r.random_list(500)
    #print(l)
    inicio = datetime.now()
    b = burbuja(l)
    print(datetime.now()-inicio)
    #print(b)