class Vehicle: 
    def Vehicle_info(self): 
        print('Inside Vehicle class') 
 
# Child class 
class Car(Vehicle): 
    def car_info(self): 
        print('Inside Car class') 
 
car = Car() 
 
# access Vehicle's info using car object 
car.Vehicle_info() 
car.car_info() 