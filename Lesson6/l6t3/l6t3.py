class Worker:
    name = ""
    surname = ""
    position = ""
    _income = dict()

    def __init__(self, Name, Surname, Position, Salary, SalaryBonus):
        self.name = Name
        self.surname = Surname
        self.position = Position
        self._income = {"Salary":int(Salary), "SalaryBonus":int(SalaryBonus)}
        return

class Position(Worker):
    def __init__(self, Name, Surname, Position, Salary, SalaryBonus):
        return super().__init__(Name, Surname, Position, Salary, SalaryBonus)

    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return self._income["Salary"] + self._income["SalaryBonus"]

p = Position("Weee", "Wooo", "Dunno", "64", "4")
print(f"{p.get_full_name()}, {p.position}, {p.get_total_income()}")
