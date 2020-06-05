monthArray = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
monthDict = {"Jan":"Winter", "Feb":"Winter", "Mar":"Spring", "Apr":"Spring", "May":"Spring", "Jun":"Summer", "Jul":"Summer", "Aug":"Summer", "Sep":"Autumn", "Oct":"Autumn", "Nov":"Autumn", "Dec":"Winter"}

while(True):
	monthNumber = input("Enter month number (press enter to exit): ")
	if monthNumber == "":
		break
	isNumberCheckFailed = True
	if(monthNumber.isdecimal()):
		monthNumber = int(monthNumber)
		if((monthNumber > 0) & (monthNumber <= 12)):
			month = monthArray[monthNumber - 1]
			print(f"{month}, {monthDict.get(month)}")
		else:
			print("Please enter value between 1 and 12")
			continue
	else:
		print("Please enter digital value between 1 and 12")
		continue
