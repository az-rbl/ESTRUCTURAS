#

import Asignacion_1 as r


class hash_table(list):
    def __init__(self,list):
        self.m = 2*len(list)
        self.valores= self.m*[None]
        self.colisiones = 0
        self.insertar_lista(list)
        
    def hash_function(self, x):
        return x%self.m
    
    def insertar(self, x):
        i = self.hash_function(x)
        if(self.valores[i]==None):
            self.valores[i]=x
        else:
            self.colisiones +=1
    
    def insertar_lista(self,list):
        for i in list:
            self.insertar(i)

if __name__== "__main__":
    import timeit
    l=r.random_list(100)
    t_0 = timeit.default_timer()
    ht =hash_table(l)
    t_1 = timeit.default_timer()
    print(t_1-t_0)
    print(ht.valores)
    print(f"Colisiones: {ht.colisiones}")
