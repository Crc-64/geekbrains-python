inFile = open("l5t3-data.txt", "r")
inData = inFile.read()
inFile.close()

employeeCount:int = 0
totalPayment:int = 0
for line in inData.splitlines():
	data = line.split()
	if(int(data[1]) < 20000):
		print(line)
	employeeCount += 1
	totalPayment += int(data[1])

avgSalary = int(totalPayment / employeeCount)
print(f"\nAverege salary: {avgSalary}")
