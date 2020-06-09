def fDiv(x, y):
    if(x == 0 or y == 0):
        return 0
    return int(x) / int(y)

inX = input("x: ")
inY = input("y: ")
result = int(fDiv(inX, inY))
print(f"result: {result}")
