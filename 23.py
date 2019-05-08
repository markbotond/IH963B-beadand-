def isprime(n):
    n=abs(int(n))

    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False

    for x in range(3,int(n**0.5)+1,2):
        if n % x == 0:
            return False
    return True

n = int(input("Hanyadik prímszámot kéred: "))

primecounter = 0
number = 1
finalprime = -1

while primecounter != n:
    if isprime(number):
        primecounter += 1
        finalprime = number
    number += 1

print(n,finalprime)