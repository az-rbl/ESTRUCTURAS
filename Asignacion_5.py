#Asignacion_5.py
#Raúl Badillo Lora
#Algoritmo de ordenamiento quick sort
#Modulo que contiene la funcion para generar una lista con valores aleatorios
import Asignacion_1 as r
#Modulo con cronometro para medir el tiempo de ejecucion
import timeit
import sys
sys.setrecursionlimit(60000)
#Funcion para dividir la lista, encuentra un pivote en medio de la lista, mientras pone los valores pequeños al inicio del arreglo
def particion(lista):
    x = lista[0]
    print(x)
    i = 1
    j = lista.index(lista[-1])
    print(lista[j])
    print(lista)
    while(True):
        while((lista[j]<= lista[0])==False):
            #print(f"{lista[j]} is bigger than {lista[0]}")
            j -=1
        while((lista[i]>=lista[0])==False and i<len(lista)-1):
            #print(f"{lista[i]} is smaller than {lista[0]}")
            i +=1
        if i < j:
            #print(lista)
            temp =lista[i]
            lista[i]  = lista[j]
            lista[j] = temp
            print(lista)
        
        #Pivote para dividir la lista
        else:
            #print(lista) 
            return j
#Regresa una lista ordenada por el algoritmo quicksort, recibe una lista
def quicksort(lista):
    if len(lista)>1:
        q=particion(lista)
        lista[:q]=quicksort(lista[:q])
        lista[q+1:]=quicksort(lista[q+1:])
    #print(lista)
    return(lista)
            
if __name__=="__main__":
    l=r.random_list(10)
    #print(l)
    t_0 = timeit.default_timer()
    b = quicksort(l)
    t_1 = timeit.default_timer()
    print(t_1-t_0)
    print(b)
                
    