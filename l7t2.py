class Clothes:
	__name:str = ""

	def __init__(self, Name):
		self.__name = Name
		return

	@property
	def Name(self):
		return self.__name

class Coat(Clothes):
	__size:int = 0

	def __init__(self, Size:int):
		self.__size = Size
		return super().__init__("Coat")

	def __str__(self):
		return f"{self.Name}, size {self.__size}"

	@property
	def clothNeeded(self):
		return (self.__size/6.5 + 0.5)


class Suit(Clothes):
	__height:int = 0

	def __init__(self, Height:int):
		self.__height = Height
		return super().__init__("Suit")

	def __str__(self):
		return f"{self.Name}, height {self.__height}"

	@property
	def clothNeeded(self):
		return (self.__height*2 + 0.3)


coat = Coat(48)
suit = Suit(180)

print(f"Cloth needed for {coat}: {coat.clothNeeded}")
print(f"Cloth needed for {suit}: {suit.clothNeeded}")
