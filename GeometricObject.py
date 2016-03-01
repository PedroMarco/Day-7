class GeometricObject:
    def __init__(self, color = "green", filled = True): ## We are defining default values
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled
  
    def __str__(self):  ##  Represents the object in python
        return "color: " + self.__color + \
            " and filled: " + str(self.__filled)
