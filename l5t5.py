fileName = "l5t5-data.txt"

inputNumbers = input("Enter numbers separated by space: ")
dataFile = open(fileName, "w")
dataFile.write(inputNumbers)
dataFile.close()

dataFile = open(fileName, "r")
data = dataFile.read()
dataFile.close()

res:int = 0
for num in data.split():
	res += int(num)

print(f"result: {res}")
