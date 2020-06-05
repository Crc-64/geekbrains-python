
array = []

print("Enter elements of an array (press enter to finish):")
while(True):
    item = input()
    if item == "":
        break
    array.append(item)

print("Plain array:")
for item in array:
    print(f"'{item}' ", end='')
print()

print("Swapped array:")
index = 0
swapped_array = []

while(index < (len(array) // 2) * 2):
    swapped_array.append(array[index + 1])
    swapped_array.append(array[index])
    index += 2
if(len(array) % 2):
    swapped_array.append(array[index])

for item in swapped_array:
    print(f"'{item}' ", end='')
print()
