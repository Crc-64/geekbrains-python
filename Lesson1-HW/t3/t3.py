isNumberCheckFailed = True
while(isNumberCheckFailed):
	in_num = input("Enter number: ")
	isNumberCheckFailed = not in_num.isdecimal()

res = int(in_num) + int(in_num+in_num) + int(in_num+in_num+in_num)
print(res)