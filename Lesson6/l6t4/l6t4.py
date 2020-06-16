from enum import Enum

class Car:
    speed = int(0)
    maxSpeed = int(0)
    color = ""
    name = ""
    is_police = False

    class TurnDirection(Enum):
        Left = 0
        Right = 1

    def __init__(self, Name, Color, Speed:int, IsPolice:bool):
        self.name = Name
        self.color = Color
        self.speed = 0
        self.maxSpeed = Speed
        self.is_police = IsPolice
        return

    def go(self):
        self.speed = self.maxSpeed
        print(f"{self.color} {self.name} gonna go")
        return

    def stop(self):
        self.speed = int(0)
        print(f"{self.color} {self.name} gonna stop")
        return

    def turn(self, Direction:TurnDirection):
        print(f"{self.color} {self.name} gonna turn {Direction.name}")
        return

    def show_speed(self):
        print(f"{self.color} {self.name} is at {self.speed} km/h")
        return


class TownCar(Car):
    __speedLimit: int = 60

    def __init__(self, Name, Color, Speed, IsPolice):
        return super().__init__(Name, Color, Speed, IsPolice)

    def show_speed(self):
        super().show_speed()
        if(self.speed > self.__speedLimit):
            print(f"  WARNING: Speed is above limit of {self.__speedLimit} km/h")
        return

class SportCar(Car):
    def __init__(self, Name, Color, Speed, IsPolice):
        return super().__init__(Name, Color, Speed, IsPolice)

class WorkCar(Car):
    __speedLimit: int = 40

    def __init__(self, Name, Color, Speed, IsPolice):
        return super().__init__(Name, Color, Speed, IsPolice)

    def show_speed(self):
        super().show_speed()
        if(self.speed > self.__speedLimit):
            print(f"  WARNING: Speed is above limit of {self.__speedLimit} km/h")
        return

class PoliceCar(Car):
    def __init__(self, Name, Color, Speed):
        return super().__init__(Name, Color, Speed, True)


townCar = TownCar("Toyota Prius", "Red", 120, False)
townCar.show_speed()
townCar.go()
townCar.show_speed()
townCar.stop()
townCar.show_speed()
townCar.turn(Car.TurnDirection.Left)
if(townCar.is_police):
    print(f"{townCar.color} {townCar.name} is a police car")
else:
    print(f"{townCar.color} {townCar.name} is not a police car")

print()

workCar = WorkCar("Volkswagen Multivan", "Black", 80, False)
workCar.go()
workCar.show_speed()
workCar.stop()
workCar.show_speed()

print()

policeCar = PoliceCar("Lamborghini Gallardo", "Yellow", 360)
policeCar.go()
policeCar.show_speed()
if(policeCar.is_police):
    print(f"{policeCar.color} {policeCar.name} is a police car")
else:
    print(f"{policeCar.color} {policeCar.name} is not a police car")
