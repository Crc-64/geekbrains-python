def capWord(inWord):
    for char in inWord:
        if char < 'a' or char > 'z':
            raise ValueError(inWord)
    return str(inWord).capitalize()

while(True):
    inStr = input("string: ").split(" ")
    try:
        newStr = ""
        for item in inStr:
            newStr += capWord(item) + " "
        print(f"result: {newStr}")
    except ValueError:
        print("String must contain only lowercased latin characters")
