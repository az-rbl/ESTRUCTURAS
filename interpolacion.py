#interpolacion.py
#Programa que busca un numero en una lista utilizanod el algoritmo de interpolación

#Fimcopm que encuentra al numero, recibe como argumentos una lista de numeros y el valor a buscar
#Devuelve como resultado la posicion del valor en la lista, o un -1 en caso de no encontrarlo
def interpolacion(lista, valor):
    i = 0
    d = len(lista)-1
    #do while
    while(lista[d]>=valor and lista[i]<valor):
        presunto =int(((valor-lista[i])/(lista[d]-lista[i]*(d-i)))+i)
        if(valor>lista[presunto]):
            i=presunto+1
        elif(valor<lista[presunto]):
            d= presunto -1
        else:
            i = presunto
    if(lista[i]== valor):
        return i
    else:
        return -1
    

if __name__== "__main__":
    import random
    import timeit
    l = list(range(100))
    v = random.randint(0,100)
    print(v)
    print("Empezando interpolacion")
    p = interpolacion(l,v)
    print(p)