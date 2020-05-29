isNumberCheckFailed = True
while(isNumberCheckFailed):
	inIncome = input("Enter income: ")
	isNumberCheckFailed = not inIncome.isdecimal()
inIncome = int(inIncome)

isNumberCheckFailed = True
while(isNumberCheckFailed):
	inExpenses = input("Enter expenses: ")
	isNumberCheckFailed = not inExpenses.isdecimal()
inExpenses = int(inExpenses)

netIncome = inIncome - inExpenses
if(netIncome > 0):
	print("Net income:", netIncome)

	isNumberCheckFailed = True
	while(isNumberCheckFailed):
		inEmployeeCount = input("Enter employee count: ")
		isNumberCheckFailed = not inEmployeeCount.isdecimal()
	inEmployeeCount = int(inEmployeeCount)

	print("Company income per employee:", netIncome/inEmployeeCount)

else:
	print("Net income is negative!")
