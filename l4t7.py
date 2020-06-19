from itertools import count
from math import factorial


def fact(n):
    res = 1
    for i in range(1, n+1):
        res *= i
        yield(res)

while(True):
    fnum = input("enter number for x! calculation:")
    if(fnum == ""):
        break
    fnum = int(fnum)
    for item in fact(fnum):
        item
    print(item)
