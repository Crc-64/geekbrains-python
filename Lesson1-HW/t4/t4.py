isNumberCheckFailed = True
while(isNumberCheckFailed):
	in_num = input("Enter number: ")
	isNumberCheckFailed = not in_num.isdecimal()

i = 0
highestNumber = 0
while(i < len(in_num)):
	if(int(in_num[i]) > highestNumber):
		highestNumber = int(in_num[i])
		if(highestNumber == 9):
			break
	i = i+1

print("Highest number: ", highestNumber)