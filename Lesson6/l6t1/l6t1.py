from time import sleep

class TrafficLight:
    __color = ["Red", "Yellow", "Green"]
    __switchTime = dict()
    __switchTime[__color[0]] = 7
    __switchTime[__color[1]] = 2
    __switchTime[__color[2]] = 20
    __currentColor = __color[0]

    def running(self):
        switchTime = self.__switchTime[self.__currentColor]
        if(self.__currentColor == self.__color[0]):
            newColor = self.__color[1]
        if(self.__currentColor == self.__color[1]):
            newColor = self.__color[2]
        if(self.__currentColor == self.__color[2]):
            newColor = self.__color[0]

        print(f"light in state '{self.__currentColor}' transitioning to '{newColor}' in {switchTime} sec")
        sleep(switchTime)
        self.__currentColor = newColor
        return 


light = TrafficLight()
print("starting traffic light")
light.running()
light.running()
light.running()
light.running()
print("--end")
