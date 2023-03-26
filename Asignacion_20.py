#Asignacion_20.py
#Raúl Badillo Lora
#Implementación de tablas hash ver-2
#En esta versión de tabla hash se resuelve el problema de colisiones.
#Se implementa una lista ligada para cada clave de entrada que genere colisión.
# Además, se implementa una función para buscar un elemento ya insertado,
# la función regresa como resultado si el elemento buscado esta en la estructura o nó.

import Asignacion_1 as r

#Clase que crea el objeto hash table, se inicializa con una lista de numeros en desorden
class hash_table(list):
    #inicializador, crea una lista valores de tamaño m= 2 * tamaño de la lista desordenada
    #Se inicializa en cero el contador de colisiones
    #Se usa la funcion insertar_lista para insertar en su lugar correspondiente a cada miembro de la lista desordenada
    def __init__(self,list):
        self.m = 2*len(list)
        self.valores= self.m*[None]
        self.colisiones = 0
        self.insertar_lista(list)
        
    # Funcion de hash = modulo(x,m)
    def hash_function(self, x):
        return x%self.m
    
    # Inserta cada valor en el indice correspondiente a su funcion hash.
    # implementa una lista ligada para cada clave de entrada que genere colisión.
    def insertar(self, x):
        i = self.hash_function(x)
        if(self.valores[i]==None):
            self.valores[i]=x
        elif isinstance(self.valores[i],list):
            self.valores[i].append(x)
            self.colisiones +=1
        else:
            self.valores[i]= [self.valores[i],x]
            self.colisiones +=1
            
    #Inserta en su lugar correspondiente a cada miembro de la lista desordenada
    def insertar_lista(self,list):
        for i in list:
            self.insertar(i)
    
    # la función regresa como resultado si el elemento buscado esta en la estructura o nó.    
    def buscar(self, elemento):
        i= self.hash_function(elemento)
        if(self.valores[i]==elemento):
            return True
        elif isinstance(self.valores[i],list):
            if elemento in self.valores[i]:
                return True
            else:
                return False
        else:
            return False

if __name__== "__main__":
    import timeit
    l=r.random_list(100)
    t_0 = timeit.default_timer()
    ht =hash_table(l)
    t_1 = timeit.default_timer()
    print(t_1-t_0)
    print(ht.valores)
    print(f"Colisiones: {ht.colisiones}")
    print(f"Se encuentra {l[0]}? {ht.buscar(l[0])}")
