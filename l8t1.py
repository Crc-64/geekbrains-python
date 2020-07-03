class Date:
	__dateString:str

	def __init__(self, DateString:str):
		self.__dateString = DateString
		return

	@classmethod
	def StrToDate(cls, dateString:str):
		return [int(item) for item in dateString.split("-")]

	@staticmethod
	def Validate(Day:int, Month:int, Year:int) -> bool:
		isValid = True
		if(Day < 1 or Day > 31):
			isValid = False
		if(Month < 1 or Month > 12):
			isValid = False
		if(Year < 0 or Year > 64000):
			isValid = False
		return isValid

strDate = "4-8-2048"
date = Date(strDate)

print(Date.StrToDate(strDate))
print(f"4-8-2020 is valid: {Date.Validate(4, 8, 2020)}")
print(f"32-13-2020 is valid: {Date.Validate(32, 13, 2020)}")
