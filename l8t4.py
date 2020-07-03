from enum import Enum

class Store:
    __equipmentByDeps = dict()

    def AddEquipment(self, Department:str, Equipment):
        try:
            equList = self.__equipmentByDeps[Department]
        except:
            equList = list()
            self.__equipmentByDeps[Department] = equList
        self.__equipmentByDeps[Department].append(Equipment)
        return


class Equipment:
    __weight:int = 0

    def __init__(self, Weight:int):
        self.__weight = Weight
        return

    @property
    def Weight(self):
        return self.__weight


class Printer(Equipment):
    class PrinterType(Enum):
       Matrix = "matrix"
       Ink = "ink"
       Laser = "laser"

    __ppm:int = 0
    __isColor:bool = False
    __type:PrinterType = None

    def __init__(self, Weight, PagesPerMinute, IsColor, Type):
        self.__ppm = int(PagesPerMinute)
        self.__isColor = bool(IsColor)
        self.__type = Printer.PrinterType(Type.lower())
        return super().__init__(int(Weight))

    def __str__(self):
        return f"Printer, {self.Weight} kg, {self.__ppm} ppm, isColor - {self.__isColor}, type - {self.__type}"


class Scaner(Equipment):
    __isDoubleSided:bool = False
    __isColor:bool = False

    def __init__(self, Weight, IsDoubleSided, IsColor):
        self.__isDoubleSided = bool(IsDoubleSided)
        self.__isColor = bool(IsColor)
        return super().__init__(int(Weight))

    def __str__(self):
        return f"Scaner, {self.Weight} kg, isDoubleSided - {self.__isDoubleSided}, isColor - {self.__isColor}"


class Xerox(Equipment):
    __isColor:bool = False
    __ppm:int = 0

    def __init__(self, Weight, PagesPerMinute, IsColor):
        self.__isColor = bool(IsColor)
        self.__ppm = int(PagesPerMinute)
        return super().__init__(int(Weight))

    def __str__(self):
        return f"Xerox, {self.Weight} kg, {self.__ppm} ppm, isColor - {self.__isColor}"


print("Available commands:")
print("  add <Department> <EquipmentType> [...]")
print("    Adds specified equipment to specified department")
print("    <Department>    - department name")
print("    <EquipmentType> - type of the equipment, available types: Printer, Scanner, Xerox")
print("      Printer <Weight> <PagesPerMinute> <IsColor> <PrinterType>")
print("        <Weight>         - weight of the printer")
print("        <PagesPerMinute> - how much pages per minute printer can do")
print("        <IsColor>        - is color printer? ('True' or 'False')")
print("        <PrinterType>    - type of the printer: Matrix, Ink, Laser")
print("      Scanner <Weight> <IsDoubleSided> <IsColor>")
print("        <Weight>         - weight of the scanner")
print("        <IsDoubleSided>  - is scanner double sided? ('True' or 'False')")
print("        <IsColor>        - is color scanner? ('True' or 'False')")
print("      Xerox <Weight> <PagesPerMinute> <IsColor>")
print("        <Weight>         - weight of the xerox")
print("        <PagesPerMinute> - how much pages per minute xerox can do")
print("        <IsColor>        - is color xerox? ('True' or 'False')")
print("  list")
print("    display all stored equipment by department")
print("  enter to exit")
print("examples:")
print("  add accounting printer 10 28 true laser")
print("  add accounting scanner 5 false true")
print("  add mgmt xerox 25 60 true")

store = Store()
while(True):
    inStr = input("#: ")
    if(inStr == ""):
        break
    args = inStr.split(" ")
    cmd = args[0].lower()
    if(cmd == "add"):
        if(len(args) <= 3):
            print("invalid args")
            continue
        type = args[2].lower()
        dep = args[1]
        try:
            if(type == "printer"):
                if(len(args) <= 6):
                    print("invalid args")
                    continue
                printer = Printer(args[3], args[4], args[5], args[6])
                store.AddEquipment(dep, printer)
            elif(type == "scanner"):
                if(len(args) <= 5):
                    print("invalid args")
                    continue
                scaner = Scaner(args[3], args[4], args[5])
                store.AddEquipment(dep, scaner)
            elif(type == "xerox"):
                if(len(args) <= 5):
                    print("invalid args")
                    continue
                xerox = Xerox(args[3], args[4], args[5])
                store.AddEquipment(dep, xerox)
        except:
            print("invalid arguments")
    elif(cmd == "list"):
        for dep in store._Store__equipmentByDeps:
            print(dep)
            for eq in store._Store__equipmentByDeps[dep]:
                print(f"\t{eq}")
