#Prueba del desempeño de los distintos algoritmos de ordenamiento
#Modulo con cronometro para medir el tiempo de ejecucion
import timeit
import Asignacion_1 as r
import Asignacion_5 as qs
import Asignacion_6 as sc
import burbuja_s as bb
import threading

size = [50, 100, 500]
ls = []
lq = []
lb =[]
for s in size:
    ts = 0
    tq = 0
    tb = 0
    threading.stack_size(2**26)
    for i in range(5):
        #print("Calculando sacudida")
        l=r.random_list(s)
        t0s = timeit.default_timer()
        a =sc.sacudida(l)
        t1s = timeit.default_timer()
        ts +=(t1s-t0s)
        #print("Calculando quicksort")
        t0q = timeit.default_timer()
        b =qs.quicksort(l)
        t1q = timeit.default_timer()
        tq +=(t1q-t0q)
        #print("Calculando burbuja")
        t0b = timeit.default_timer()
        c =bb.burbuja(l)
        t1b = timeit.default_timer()
        tb +=(t1b-t0b)
    #print("calculando promedios")
    ps = ts/5
    ls.append(ps)
    lq.append(tq/5)
    lb.append(tb/5)
print(ls,lq,lb)


