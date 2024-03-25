from abc import ABC, abstractmethod
class shape:
    def __init__(self,name,color):
        self.name=name
        self.__color=color

    def get_color(self):
        return self.__color
    
    def set_color(self,color):
        self.__color = color

    @abstractmethod
    def calculate_area(self):
        pass

#############################    
class Circle(shape):
    def __init__(self,radius,color):
        super().__init__('Circle',color)
        self._radius = radius

    def calculate_area(self):
        area = 3.14*self._radius * self._radius
        return area 
    
#################################
class Square(shape):
    def __init__(self, length, color):
        super().__init__('square',color)
        self._length = length

    def calculate_area(self):
        return self._length * self._length
#####################################    
class Rectangle(shape):
    def __init__(self,length,width,color):
        super().__init__('rectangle',color)
        self._length = length
        self._width = width

    def calculate_area(self):
        area  = self._length * self._width
        return area

circle = Circle(5,'red')
square = Square(5,'blue')
rectangle = Rectangle(5,5,'yellow')


print(f"{circle.name} with color {circle.get_color()}: {circle.calculate_area()}")

    
print(f"{square.name} with color {square.get_color()}: {square.calculate_area()}")


print(f"{rectangle.name} with color {rectangle.get_color()}: {rectangle.calculate_area()}")



########################################################################################


