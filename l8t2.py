class MyZeroDivException(Exception):
	def __init__(self, *args):
		if(args):
			if(args[0]["B"] != 0):
				args[0]["Res"] = args[0]["A"] / args[0]["B"]
			else:
				args[0]["ZeroDiv"] = True
			self.message = "Done"
		else:
			self.message = None

	def __str__(self):
		if(self.message):
			return f"{self.message}"
		else:
			return "MyZeroDivException: no message supplied."

print("Enter A, B to div, enter to exit")
while(True):
	argA = input("A: ")
	if(argA == ""):
		break
	argB = input("B: ")
	if(argB == ""):
		break;

	divArgs = {"A":int(argA), "B":int(argB), "Res":int(0), "ZeroDiv":False}
	try:
		raise MyZeroDivException(divArgs)
	except MyZeroDivException:
		if(divArgs["ZeroDiv"]):
			print("Div by zero!", end = "\n\n")
		else:
			print(f"A / B = {divArgs['Res']}", end = "\n\n")
