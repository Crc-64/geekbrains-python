class Road:
    _length = 0
    _width = 0
    __oneCmWeight = 25
    __thicknessInCm = 5

    def __init__(self, Length, Width):
        self._length = Length
        self._width = Width
        return

    def RoadWeight(self):
        return self._length * self._width * self.__oneCmWeight * self.__thicknessInCm


road = Road(20, 5000)
weight = road.RoadWeight()
print(f"{weight}")