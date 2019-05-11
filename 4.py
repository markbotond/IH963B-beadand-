#4. Feladat
#Írjon függvényt, amely paraméterként megkapja egy érvényes dátum három egész
#értékű komponensét: egy évszámot, egy hónapszámot és egy napszámot, ebben a
#sorrendben! A függvény visszatérési értéke legyen az az egész szám, amely jelzi, hogy
#mennyit kell még aludni a Télapó következő látogatásáig (1 alvás/éjszaka értékkel
#számolva és a napközbeni alvásoktól eltekintve)!

from datetime import date
def szamolo(year,month,day):
    ma = date(year,month,day)
    mikulas = date(year,12,6)
    nov = mikulas.year+1
    nextyear = date(nov,12,6)
    if ma > mikulas:
        mikulas = nextyear
        delta = mikulas - ma
        return delta.days
    else:
        delta = mikulas - ma
        return delta.days

print(szamolo(2018,12,1))
