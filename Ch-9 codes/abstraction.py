from abc import ABC,abstractmethod

class Shape(ABC):
    def __init__(self,shape_name):
        self.shape_name=shape_name
    
    @abstractmethod
    def draw(self):
        pass
    
class Circle(Shape):
    def __init__(self):
        super().__init__('circle')
    def draw(self):
        print("It is Circle")
        
c=Circle()
c.draw()

# s=Shape("xyz")
# s.draw() We can't call object of Abstract clasS