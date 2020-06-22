class Matrix:
    def __init__(self, elementList):
        self.elements = elementList
        self.mxH = len(elementList)
        self.mxW = len(elementList[0])

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.elements]))

    def __add__(self, matrix):
        newMx = Matrix(self.elements)
        if((self.mxH != matrix.mxH) or (self.mxW != matrix.mxW)):
            raise ValueError("Cannot add matrixes with different dimensions.")

        for i in range(self.mxH):
            for j in range(self.mxW):
                newMx.elements[i][j] += matrix.elements[i][j]
        return newMx


mx1 = Matrix([[ 3,  5, 32, 4],
              [ 2,  4,  6, 2],
              [-1, 64, -8, 8]])

mx2 = Matrix([[ 2, 8, 16, 8],
              [16, 0, 16, 2],
              [16, 8, 2,  4]])

print(f"matrix 1:\n{mx1}")
print()
print(f"matrix 2:\n{mx2}")
print()

mx3 = mx1.__add__(mx2)
print(f"mx1 + mx2:\n{mx3}")
