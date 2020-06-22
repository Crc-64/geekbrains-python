dataFile = open("l5t6-data.txt")
data = dataFile.read()
dataFile.close()

def GetInt(strInt) -> int:
	if(strInt.isdecimal()):
		return int(strInt)
	if(strInt == "-"):
		return 0
	digits:int = 0
	for char in strInt:
		if(char.isdecimal()):
			digits += 1
		else:
			break
	return int(strInt[:digits])

res = dict()
for line in data.splitlines():
	name, lectH, practH, labH = line.split()
	name = name.replace(":", "")
	lectH = GetInt(lectH)
	practH = GetInt(practH)
	labH = GetInt(labH)
	try:
		prevVal = res[name]
	except:
		prevVal:int = 0
	res[name] = prevVal + lectH + practH + labH

print(res)