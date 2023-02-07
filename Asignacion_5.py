#Asignacion_5.py
#Raúl Badillo Lora
#Algoritmo de ordenamiento quick sort
#Modulo que contiene la funcion para generar una lista con valores aleatorios
import Asignacion_1 as r
#Modulo con cronometro para medir el tiempo de ejecucion
import timeit

#Funcion para dividir la lista, encuentra un pivote en medio de la lista, mientras pone los valores pequeños al inicio del arreglo
def particion(lista,p,r):
    x = lista[p]
    i = p
    j = r-1
    while(True):
        while((lista[j]<= x)==False):
            j -=1
        while((lista[i]>=x)==False):
            i +=1
        if i < j:
            temp =lista[i]
            lista[i]  = lista[j]
            lista[j] = temp
        #Pivote para dividir la lista
        else: return j
#Regresa una lista ordenada por el algoritmo quicksort, recibe una lista
def quicksort(lista:list, p =0, r = None):
    if r == None: r=len(lista)
    if p < r:
        q=particion(lista, p,r)
        quicksort(lista,p,q)
        quicksort(lista, q+1, r)
    return(lista)
            
if __name__=="__main__":
    l=r.random_list(10)
    print(l)
    t_0 = timeit.default_timer()
    b = quicksort(l)
    t_1 = timeit.default_timer()
    print(t_1-t_0)
    print(b)
                
    