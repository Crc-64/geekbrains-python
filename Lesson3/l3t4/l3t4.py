def myPow(x, n):
    if (n == 0):
        return 1
    res = 1
    i = abs(n)
    while(i > 0):
        res = res * x
        i -= 1
    if(n < 0):
        res = 1 / res
    return res

while(True):
    inX = float(input("x: "))
    inPow = int(input("pow: "))
    result = myPow(inX, inPow)
    print(f"result: {result}")
