outFile = open("l5t1-out.txt", "w")

print("Enter any text, it will be written to 'out.txt'. Empty line to exit")
while(True):
	strLine = input("#: ")
	if(strLine == ""):
		break
	outFile.write(strLine + "\n")
outFile.close()
