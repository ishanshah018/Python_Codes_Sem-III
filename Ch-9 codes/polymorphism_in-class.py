# It is used when we group different objects having same methods 
# We can add object of different class to tuple or list and using for loop and iterate over them

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
        
fer=Ferrari()
bm=BMW()

for car in(fer,bm):
    car.fuel_type()
    car.max_speed()