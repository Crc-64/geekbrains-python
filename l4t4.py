srcList = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
dstList = [item for item in srcList if srcList.count(item) == 1]

print(f"src: {srcList}")
print(f"dst: {dstList}")
