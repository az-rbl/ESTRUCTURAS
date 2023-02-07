#Modulo que contiene la funcion para generar una lista con valores aleatorios
import Asignacion_1 as r
import timeit

#Regresa una lista ordenada por el algoritmo sacudida, recibe una lista
def sacudida(lista):
    izq=0
    dcha=len(lista)-1
    k= len(lista)-1
    while(izq<dcha):
        #print("Entre en while")
        for i in range(dcha,izq,-1):
            if lista[i]< lista[i-1]:
                #print("Entre en if")
                temp, lista[i] = lista[i], lista[i-1]
                lista[i-1] = temp
                k = i
        izq= k+1
        for i in range(izq,dcha):
            if lista[i]< lista[i-1]:
                temp, lista[i] = lista[i], lista[i-1]
                lista[i-1] = temp
                k=i
            dcha=k-1
    return lista
            
if __name__=="__main__":
    l=r.random_list(10)
    #print(l)
    t_0 = timeit.default_timer()
    b = sacudida(l)
    t_1 = timeit.default_timer()
    print(t_1-t_0)
    #print(b)
                
    