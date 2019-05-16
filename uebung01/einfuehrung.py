##
#   Aufgabe 1
##

##
#c)

#sqrt ist teil des math Moduls und ist wie folgt zu importieren und zu verwenden:
import math
print(math.sqrt(4))

#bei negativen Zahlen entsteht ein math domain error
#print(math.sqrt(-4))

#die gewunschten Funktionen
def mysqrt(x):
    if x<0:
        print("mysqrt funktioniert nicht für negative Zahlen, du Dussel!")
    else:
        return print(math.sqrt(x))

def mysqrt2(x):
    try:
        return print(math.sqrt(x))
    except:
        print("mysqrt funktioniert nicht für negative Zahlen, du Dussel!")
#die Anwendung
mysqrt(9) #gibt drei zurück
mysqrt(-25) #gibt eine fehlermeldung zurück

#Schleife:
for i in range(-10,10+1):
    print("Zahl", i)
    #Der Modulooperator führt eine Division mit Rest aus, und gibt den Rest zurück
    print("Modulo 5  = ", i%5)

#Man sollte Strings in dreifache Anführungszeichen einschließen, wenn man einfache und doppelte
#Anführungszeichen sorglos verwenden möchte (solange man dies nicht dreifach tut ;-) )
#Ebenso verwendung für Dokumentationen von Funktionen und Klassen

#Die Klasse List entspricht einem Array bzw. std::vector in c++, den einzelnen Feldern ist ein index zugeordnet, die Klasse dict entspricht dagegen
#der std::map in C++, den einzelnen Feldern sind key´s zugeordnet

#die init Funktion wird aufgerufen sobald ein Objekt von einer Klasse instansiiert wird. Sie wird
#in der regel dazu verwendet das Objekt zu initialisieren. Verwendung erfolgt beim korrekten Initialisieren automatisch "ohne" zutun

#d)
