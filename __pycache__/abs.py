from abc import ABC, abstractmethod

class Shape(ABC):   #abstract base class
    @abstractmethod 
    def area(self): 
        pass

class rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
rectangle = rectangle(5, 10)
print(f"Area of rectangle: {rectangle.area()}")    