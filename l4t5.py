from functools import reduce

def mul(a:int, b:int):
    return a*b

evenList = [item for item in range(99, 1001) if item % 2 == 0]
print(f"even numbers list: {evenList}", end="\n\n")

result = reduce(mul, evenList)
print(f"result: {result}")