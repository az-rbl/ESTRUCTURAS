#Prueba del desempeño de los distintos algoritmos de ordenamiento
#Modulo con cronometro para medir el tiempo de ejecucion
import timeit
import Asignacion_4 as bi
import secuencial as sc
import secuencial_s as ss
import pandas as pd
import interpolacion as ip

import random
size = [50, 100, 500, 1000, 5000, 10000, 20000, 50000, 100000, 200000]
lsc = []
lss = []
lbi =[]
lip = []
for s in size:
    tsc = 0
    tss = 0
    tbi = 0
    tip = 0
    for i in range(5):
        #print("Calculando sacudida")
        l=list(range(s))
        n = random.randint(0,s)
        t0s = timeit.default_timer()
        a =sc.secuencial(l,n)
        t1s = timeit.default_timer()
        tsc +=(t1s-t0s)
        #print("Calculando quicksort")
        t0q = timeit.default_timer()
        b =ss.secuencial(l,n)
        t1q = timeit.default_timer()
        tss +=(t1q-t0q)
        #print("Calculando burbuja")
        t0b = timeit.default_timer()
        c =bi.binario(l,n)
        t1b = timeit.default_timer()
        tbi +=(t1b-t0b)
        t0i = timeit.default_timer()
        d = ip.interpolacion(l,n)
        t1i = timeit.default_timer()
        tip += (t1i-t0i)        
    #print("calculando promedios")

    lsc.append(tsc/5)
    lss.append(tss/5)
    lbi.append(tbi/5)
    lip.append(tip/5)
    df = pd.DataFrame({'secuencial':lsc,
                     'sentinela': lss,
                     'binario':lbi,
                     'interpolacion':lip})

df.to_csv('file.csv', index=False)


