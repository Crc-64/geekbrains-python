import random
random.seed()

maxItems = int(16)
items = list()
newItems = list()

i = 0
while i < maxItems:
    items.append(random.randint(0, 256))
    i += 1

i = 0
while i < len(items) - 1:
    if(items[i] < items[i + 1]):
        newItems.append(items[i + 1])
    i += 1

print(f"src: {items}")
print(f"dst: {newItems}")

