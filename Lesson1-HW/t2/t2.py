isNumberCheckFailed = True
while(isNumberCheckFailed):
	in_num = input("Enter time in seconds: ")
	isNumberCheckFailed = not in_num.isdecimal()

in_num = int(in_num)
hours = in_num//3600
minutes = in_num//60 - hours*60
seconds = in_num%60
print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
