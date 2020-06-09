res = int(0)

print("Enter values separated by space, use '!' to finish")
doExit = False
while(not doExit):
    inValues = input("#: ").split(" ")
    for item in inValues:
        if item == "!":
            doExit = True
            break
        else:
            res += int(item)
    print(f"result: {res}")