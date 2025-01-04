# A normal function that take any object of class as a parameter and execute its method without checking its class type

class Ferrari:
    def fuel_type(self):
        print("Petrol")
    
    def max_speed(self):
        print("Max speed is 350")
        
class BMW:
    def fuel_type(self):
        print("Diesel")
    
    def max_speed(self):
        print("Max speed is 240")
        
# Normal Function that takes any object of class as a parameter

def car_details(obj):
    obj.fuel_type()
    obj.max_speed()   
        
fer=Ferrari()
bm=BMW()

car_details(fer)
car_details(bm)