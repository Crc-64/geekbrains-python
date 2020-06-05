
array = [int(7), int(5), int(3), int(3), int(2)]

print(f"Stock array: ", end="")
for item in array:
    print(f"{item} ", end="")
print()

while(True):
    newItem = input("Enter number (press enter to finish): ")
    if newItem == "":
        break
    newItem = int(newItem)

    index = len(array) - 1
    inserted = False
    while index >= 0:
        if(array[index] > newItem):
            array.insert(index + 1, newItem)
            inserted = True
            break;
        index -= 1
    if(not inserted):
        array.insert(0, newItem)

    print("Array: ", end="")
    for item in array:
        print(f"{item} ", end="")
    print()
