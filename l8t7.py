class myComplexNumber:
    a: int = 0
    b: int = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b
        return

    def __add__(self, other):
        return myComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return myComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

    def __str__(self) -> str:
        return f"{self.a} " + ("+" if (self.b >= 0) else "-") + f" {abs(self.b)}i"

 
cn1 = myComplexNumber(2, 10)
cn2 = myComplexNumber(3, 5)

print(f"cn1: {cn1}")
print(f"cn2: {cn2}")
print(f"cn1 + cn2 = {cn1 + cn2}")
print(f"cn1 * cn2 = {cn1 * cn2}")
