#  Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

vehicle = Vehicle(120, 15000)

print("Max Speed: ",vehicle.max_speed)
print("Mileage: ",vehicle.mileage)
