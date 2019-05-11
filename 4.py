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

print(szamolo(2018,12,2))
