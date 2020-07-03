class MyList:
    __list = list()

    def __init__(self):
        return

    def AddItem(self, item):
        try:
            self.__list.append(int(item))
        except ValueError:
            # вообще так делать не культурно, но по тексту задания...
            print("specified value is not decimal")
        return

itemList = MyList()
print("enter elements for the list one by one, enter to stop")
while(True):
    inStr = input("#: ")
    if(inStr == ""):
        break
    itemList.AddItem(inStr)

print(itemList._MyList__list)
