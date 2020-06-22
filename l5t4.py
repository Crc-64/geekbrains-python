inFile = open("l5t4-in.txt", "r")
outFile = open("l5t4-out.txt", "w")

names = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

for line in inFile:
	src = line.split()[0]
	dst = names[src]
	newStr = line.replace(src, dst)
	outFile.write(newStr)
	print(newStr, end = "")
print()