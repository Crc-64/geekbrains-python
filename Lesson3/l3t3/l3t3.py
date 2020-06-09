def my_func(x, y, z):
    inMin = min(x, y, z)
    a = x if x != inMin else y
    b = z if z != inMin else y
    return int(a) + int(b)

while(True):
    x = input("x: ")
    y = input("y: ")
    z = input("z: ")
    res = my_func(x, y, z)
    print(f"result: {res}")
