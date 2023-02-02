import Asignacion_1 as r
import timeit

def secuencial(lista, valor):
    posicion = -1
    for i in range(len(lista)-1):
        if valor ==lista[i]:
            posicion = i
    return posicion

if __name__=="__main__":
    l=r.random_list(50,0,10)
    #print(l)
    t_0 = timeit.default_timer()
    b = secuencial(l,3)
    t_1 = timeit.default_timer()
    print(t_1-t_0)
    print(b)