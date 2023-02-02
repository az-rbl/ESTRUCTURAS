import Asignacion_1 as r
import timeit
import burbuja_s

def secuencial(lista, valor):
    posicion = -1
    for i in range(len(lista)-1):
        if valor ==lista[i]:
            posicion = i
        if lista[i]>valor:
            break
    return posicion

if __name__=="__main__":
    l=r.random_list(50,0,10)
    l= burbuja_s.burbuja(l)
    #print(l)
    t_0 = timeit.default_timer()
    b = secuencial(l,3)
    t_1 = timeit.default_timer()
    print(t_1-t_0)
    print(b)