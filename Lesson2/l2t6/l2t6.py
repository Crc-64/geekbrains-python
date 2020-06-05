print("Available commands:")
print("add Name Price Amount AmountType")
print("  adds item to list, where")
print("    Name       - item name")
print("    Price      - price of an item")
print("    Amount     - number of items being added")
print("    AmountType - type of the unit that is added")
print("list")
print("  shows the list and analysis")
print()


goods = [
(1, {"name": "computer", "price": 20000, "amount": 5, "amountType": "unit"}),
(2, {"name": "printer", "price": 6000, "amount": 2, "amountType": "unit"}), 
(3, {"name": "scanner", "price": 2000, "amount": 7, "amountType": "unit"})
]

while(True):
    commandLine = input("Enter command (press enter to exit): ")
    commandArgs = commandLine.split(" ")
    command = commandArgs[0].lower()
    
    if command == "":
        break

    if command == "add":
        newDic = dict()
        newDic["name"] = commandArgs[1]
        newDic["price"] = int(commandArgs[2])
        newDic["amount"] = int(commandArgs[3])
        newDic["amountType"] = commandArgs[4]
        t = tuple((len(goods) + 1, newDic))
        goods.append(t)
        continue

    if command == "list":
        distinctNames = set()
        distinctPrices = set()
        distinctAmounts = set()
        distinctAmountTypes = set()

        for item in goods:
            distinctNames.add(item[1]["name"])
            distinctPrices.add(item[1]["price"])
            distinctAmounts.add(item[1]["amount"])
            distinctAmountTypes.add(item[1]["amountType"])
            print(f"{item}")
        print()

        print("Analytics:")
        analytics = dict()
        analytics["name"] = distinctNames
        analytics["price"] = distinctPrices
        analytics["amount"] = distinctAmounts
        analytics["amountTypes"] = distinctAmountTypes
        for item in analytics:
            print(f"{item}: {analytics[item]}")
        print()
