highestPalindrom = -1
highestPalindromX = -1
highestPalindromY = -1
for i in range(9999,1000,-1):
    for j in range(9999,1000,-1):
        multply = i*j
        stringofmultiply = str(multply)
        if len(stringofmultiply) % 2 == 0:
            leftside = stringofmultiply[0:4]
            rightside = stringofmultiply[4:8]
            reverserightside = rightside[::-1]

            if (leftside == reverserightside) and multply > highestPalindrom:
                highestPalindrom = multply
                highestPalindromX = i
                highestPalindromY = j

print("legnagyobb palindrom:",highestPalindrom,"szorzótényezők",highestPalindromX,highestPalindromY)