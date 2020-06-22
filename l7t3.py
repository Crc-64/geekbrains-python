class Cell:
	__cells:int = 0

	@property
	def Cells(self):
		return self.__cells

	def __init__(self, Cells:int):
		self.__cells = Cells
		return

	def __add__(self, otherCell):
		return Cell(self.Cells + otherCell.Cells)

	def __sub__(self, otherCell):
		result = self.Cells - otherCell.Cells
		if(result <= 0):
			raise ValueError("Result cell count cannot be negative!")
		return Cell(result)

	def __mul__(self, otherCell):
		return Cell(self.Cells * otherCell.Cells)

	def __truediv__(self, otherCell):
		return Cell(int(self.Cells / otherCell.Cells))

	def __str__(self):
		return f"{self.Cells}"

	def make_order(self, Rows:int) -> str:
		return ("\n".join(["*" * Rows for rows in range(int(self.Cells / Rows))])) + "\n" + ("*" * int(self.Cells % Rows))

cell1 = Cell(64)
cell2 = Cell(8)

print(f"Cell 1 cells count: {cell1.Cells}")
print(f"Cell 2 cells count: {cell2.Cells}")
print(f"cell 1 + cell 2 = {cell1 + cell2}")
print(f"cell 1 - cell 2 = {cell1 - cell2}")
print(f"cell 1 * cell 2 = {cell1 * cell2}")
print(f"cell 1 / cell 2 = {cell1 / cell2}")

print("\nCell 1 with cells in row 10:")
print(cell1.make_order(10))
