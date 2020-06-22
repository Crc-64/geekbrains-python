import json

companies = dict()
totalCompanies:int = 0
totalProfit:int = 0

with open("l5t7-data.txt", "r") as inFile:
	for line in inFile:
		name, typeOfOwnership, income, expenses = line.split()
		income = int(income)
		expenses = int(expenses)
		netIncome = income - expenses

		totalCompanies += 1
		if(netIncome > 0):
			totalProfit += netIncome

		companies[name] = netIncome

resList = list()
resList.append(companies)

avgProfitDict = dict()
avgProfitDict["average_profit"] = int(totalProfit / totalCompanies)
resList.append(avgProfitDict)

print(f"{resList}")

with open("out.json", "w") as outFile:
	json.dump(resList, outFile, sort_keys = True, indent = 4)
	outFile.close()
