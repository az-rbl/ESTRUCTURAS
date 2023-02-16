#Asignacion_5.py
#Raúl Badillo Lora
#Algoritmo de ordenamiento quick sort
#Modulo que contiene la funcion para generar una lista con valores aleatorios
import Asignacion_1 as r
#Modulo con cronometro para medir el tiempo de ejecucion
import time

#Funcion para dividir la lista, encuentra un pivote en medio de la lista, mientras pone los valores pequeños al inicio del arreglo
def particion(lista,p,r):
    x = lista[r]
    i = p-1
    j = p
    while j <= r-1:
        if lista[j] <= x:
            i = i + 1
            temp =lista[i]
            lista[i]  = lista[j]
            lista[j] = temp
        j = j + 1
    temp =lista[i+1]
    lista[i+1]  = lista[r]
    lista[r] = temp
    return i+1

#Regresa una lista ordenada por el algoritmo quicksort, recibe una lista
def quicksort(lista, p , r ):
    if p < r:
        q = particion(lista, p,r)
        quicksort(lista,p, q-1)
        quicksort(lista, q+1, r)



if __name__=="__main__":
    tam = 500000
    import sys
    print(sys.getrecursionlimit()) # Prints 1000
    sys.setrecursionlimit(2000)
    print(sys.getrecursionlimit())

    l=r.random_list(tam)
    #print(l)
    t_0 = time.time()

    print('tiempo_1:', t_0)
    print('tamaño de la lista:', len(l))

    quicksort(l,0,len(l)-1)

    t_1 = time.time()
    print('tiempo_2:', t_1)

    print('\n tiempo en milisegundos:', t_1-t_0)
    #print(l)
