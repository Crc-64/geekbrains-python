str = input("Enter some words: ")

strArray = str.split(" ")
index = 0
for item in strArray:
    print(f"{index}: {item[0:10]}")
    index += 1
    