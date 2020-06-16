class Stationery:
    _title = ""

    def __init__(self, Title: str):
        self._title = Title
        return

    def draw(self):
        print(f"Starting to draw with {self._title}")
        return

class Pen(Stationery):
    def draw(self):
        print(f"Weee Wooo !!! Starting to draw with Pen!")
        return

class Pencil(Stationery):
    def draw(self):
        print(f"Weee Wooo !!! Starting to draw with Pencil!")
        return

class Handle(Stationery):
    def draw(self):
        print(f"Weee Wooo !!! Starting to draw with Handle!")
        return


pen = Pen("Blue pen")
pen.draw()
pencil = Pencil("Red pencil")
pencil.draw()
handle = Handle("Black handle")
handle.draw()
hotIron = Stationery("Hot Iron")
hotIron.draw()