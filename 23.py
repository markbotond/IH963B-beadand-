#23. Feladat
#Listázva az első hat prímszámot a következőket kapjuk: 2, 3, 5, 7, 11, és 13, ahol a 13
#a 6. prímszám. Írjon programot, amely meghatározza az N. prímszámot. Készítsen
#hatékony implementációt, amely akár valós időben a 10 000. prímszámot is képes
#kiszámolni.


def isprime(n):
    n=abs(int(n))

    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for x in range(3,int(n**0.5)+1,2):
        if n % x == 0:
            return False
    return True

n = int(input("Hanyadik prímszámot kéred: "))

primecounter = 0
number = 1
finalprime = 0

while primecounter != n:
    if isprime(number):
        primecounter += 1
        finalprime = number
    number += 1

print(n,finalprime)
