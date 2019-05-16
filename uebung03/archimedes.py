import math

def archimedes1():
    k = 4
    s = math.sqrt(2)
    t = 2
    unten = (k / 2) * s
    oben  = (k / 2) * t

    print("Anzahl k: ", k)
    print("Seitenlänge innen: ", s)
    print("Seitenlänge außen: ", t)
    print("oberer Pi Wert: ", oben)
    print("unterer Pi Wert: ", unten)

archimedes1()
