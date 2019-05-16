
###
#
# a)
# Es gibt 14 möglichkeiten (7 Wochentage * 2 (Schaltjahr und Keines)).
# Alle Tage eines Jahres stehen fest wenn man weiß mit welchem Wochentag das Jahr beginnt
# und ob es ein Schaltjahr ist oder nicht.
# Die 14 Möglichkeiten für den 1.Jannuar sind daher:
# Kein Schaltjahr: Montag, Dienstag, Mittwoch, Donnerstag, Freitag, Samstag, Sonntag
# Schaltjahr: Montag, Dienstag, Mittwoch, Donnerstag, Freitag, Samstag, Sonntag
#
# Zusatzfakt:
# Alle 28 Jahre sind die Kalenderjahre und ihre abfolge identisch (Achtung bei Jahrhundert wenden,
# wenn die Jahrhundertzahl nicht durch 4 Teilbar ist wird der nächste 28 Jahre zyklus neu begonnen ),
# dass ergibt sich weil sich die Wochentage alle 7 Jahre wiederholen und alle 4 Jahre ein Schaltjahr eintritt (7*4).
#
#

###
#
# b)
#
#
import calendar

def friday13th():
    
    Kalender = calendar.Calendar()
    
    def friday13(start, end):
        zahler = 0
        for jahr in range(start, end):
            for monat in range(1, 13):
                for tag in Kalender.itermonthdays2(jahr, monat):
                    if tag[0] == 13 and tag[1] == 4:
                        zahler = zahler + 1
    #print(zahler)
        return zahler

    k = 0
    # Keine Schaltjahre
    k = k + friday13(2018, 2019)
    print("\nKeine Schaltjahre: \n Montag: ", friday13(2018, 2019))
    k = k + friday13(2019, 2020)
    print(" Dienstag: ", friday13(2019, 2020))
    k = k + friday13(2025, 2026)
    print(" Mittwoch: ", friday13(2025, 2026))
    k = k + friday13(2026, 2027)
    print(" Donnerstag: ", friday13(2026, 2027))
    k = k + friday13(2021, 2022)
    print(" Freitag: ", friday13(2021, 2022))
    k = k + friday13(2022, 2023)
    print(" Samstag: ", friday13(2022, 2023))
    k = k + friday13(2023, 2024)
    print(" Sonntag: ", friday13(2023, 2024))
    # Schaltjahre
    k = k + friday13(1996, 1997)
    print("\nSchaltjahre: \n Montag: ", friday13(1996, 1997))
    k = k + friday13(2008, 2009)
    print(" Dienstag: ", friday13(2008, 2009))
    k = k + friday13(2020, 2021)
    print(" Mittwoch: ", friday13(2020, 2021))
    k = k + friday13(2004, 2005)
    print(" Donnerstag: ", friday13(2004, 2005))
    k = k + friday13(2016, 2017)
    print(" Freitag: ", friday13(2016, 2017))
    k = k + friday13(2000, 2001)
    print(" Samstag: ", friday13(2000, 2001))
    k = k + friday13(2040, 2041)
    print(" Sonntag: ", friday13(2040, 2041))

    print("\nGesamt: ", k)

friday13th()

###
#
# c)
#
#

def friday13thSince(day, month, year):
    Kalender = calendar.Calendar()
    
    prezahler = 0 #Zählt wie viele Freitag 13 im Jahr vor dem Datum geschehen
    
    for monat in range(1, month+1): #Monate vor dem Datums Monat
        for tag in Kalender.itermonthdays2(year, monat):
            if tag[0] == 13 and tag[1] == 4: #Freitag der 13. die erfasst wurden vor dem Tag des Datums
                if day<=13 and month == monat:
                    prezahler = prezahler + 0
                else:
                    prezahler = prezahler + 1

    zahler = prezahler * -1

    for jahr in range(year, 2020):
        for monat in range(1, 13):
            for tag in Kalender.itermonthdays2(jahr, monat):
                if tag[0] == 13 and tag[1] == 4:
                    zahler = zahler + 1

# Minus 2 weil zwei freitag der 13. nach April in 2019 stattfinden
    zahler = zahler - 2
    if zahler<0:
        print(0)
    else:
        print("\nSeit dem", day, month, year, "aufgetretene friday13th:", zahler, "\n")

    return zahler 

friday13thSince(24, 10, 1999)
