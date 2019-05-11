#22. Feladat
#Egy palindrom szám olyan, hogy mindkét végéről kezdve olvasva a számot, ugyan azt
#az értéket kapjuk. A legnagyobb palindrom szám, amely előáll két 2-számjegyű szám
#szorzataként az a 9009 = 91 × 99. Írjon programot, amely megkeresi a legnagyobb
#palindrom számot amely előáll két 4-jegyű szám szorzataként.
#Legnagyobb palindrom szám: 99000099, 2db 4 számjegyű szorzat: 9999 * 9901

highestPalindrom = -1
highestPalindromX = -1
highestPalindromY = -1
for i in range(9999,999,-1):
    for j in range(9999,999,-1):
        multply = i*j
        stringofmultiply = str(multply)
        leftside = stringofmultiply[0:4]
        rightside = stringofmultiply[4:8]
        reverserightside = rightside[::-1]

        if (leftside == reverserightside) and multply > highestPalindrom:
            highestPalindrom = multply
            highestPalindromX = i
            highestPalindromY = j

print("legnagyobb palindrom:",highestPalindrom,"szorzótényezők:",highestPalindromX,"*",highestPalindromY)
