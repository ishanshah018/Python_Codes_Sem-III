class Vehicle:
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price
        
    def show(self):
        print("Details: ",self.name,self.color,self.price)
    
    def max_speed(self):
        print("Max speed is 150 km/hr")
        
    def change_gear(self):
        print("It changes 6 gears")
        
class Car(Vehicle):
    
    def max_speed(self):
        print("Max speed is 220 km/hr")
        
    def change_gear(self):
        print("It changes 7 gears")
        
c=Car("BMW","Red",8000000)
c.show()
c.max_speed()
c.change_gear()
print("___________________________")
v=Vehicle("Truck","White",3300000)
v.show()
v.max_speed()
v.change_gear()