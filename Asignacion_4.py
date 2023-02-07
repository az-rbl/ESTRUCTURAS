#Modulo que contiene la funcion para generar una lista con valores aleatorios
import Asignacion_1 as r
#Modulo con timer para medir el tiempo de ejecucion
import timeit
#Modulo con el algoritmo de otdenamiento burbuja
import burbuja_s

#Modulo que encuentra un valor en una lista utilizando el algoritmo de busqueda binaria busqueda binaria
def binario(lista, valor):
    encontrado =  False
    izq = 0
    der = len(lista)-1
    c = 0
    while(izq < der) and (encontrado == False):
        medio =int((izq+der)/2)

        if lista[medio] == valor:
            encontrado = True
            return medio
        elif lista[medio] > valor:
           
            der = medio-1
        else:

            izq = medio+1

if __name__=="__main__":
    l=r.random_list(50,0,10)
    l= burbuja_s.burbuja(l)
    print(l)

    t_0 = timeit.default_timer()
    b = binario(l,3)
    t_1 = timeit.default_timer()
    print(t_1-t_0)
    print(b)            