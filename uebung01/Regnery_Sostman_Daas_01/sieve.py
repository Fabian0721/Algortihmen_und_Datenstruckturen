import math


def sieve(maximalwert):
    #Feld erzeugen der gewünschten länge
    feld = [True] * maximalwert
    #0 und 1 sind keine Primzahlen
    feld[0] = feld[1] = False
    #Algorithmus
    for i in range(2,int(math.sqrt(maximalwert))+1):
        if feld[i]:
            for k in range(i*i, maximalwert, i):
                feld[k] = False
    #Primzahl Array erstellen
    ruckgabe = list()
    for i in range(0, len(feld)):
        if feld[i]:
            ruckgabe.append(i)
            #Druck im Terminal zur Kontrolle
#print(i)
    return ruckgabe
    
