#Asignacion_1.py 
# Generación de números aleatorios
#Implementar una función o métodopara que se generen números aleatorios con las siguientes restricciones:
#    Que el usuario proporcione cómo datos de entrada el rango en el que desea generar estos numeros (por ejemplo: números entre 0 y 20,000) 
#    Que indique cuantos números desea generar (por ejemplo: 500 numero).
#Estos números aleatorios deben almacenarse en un arreglo dinámico.

#Modulo para generar numeros aleatorios
import random

#Funcion que genera una lista aleatoria, recibe 3 valores: size, el tamaño de la lista; being el inicio del rango de los numeros; y end, el final del rango de numeros aleatorios
def random_list(size, begin=0, end=1000):
    lista = [random.randint(begin,end)for x in range (size)]
    return lista

if __name__=="__main__":
    ri=input("Inicio rango ")
    rf=input("Fin rango ")
    nu = input("Numeros a generar ")
    print(random_list(int(nu), int(ri), int(rf)))
    