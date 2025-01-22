# Base class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def describe(self):
        print("This is a", self.brand, self.model)

# Derived class
class Car(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model)  # Call the base class constructor
        self.year = year

    def describe(self):
        # Call the base class 'describe' method
        super().describe()
        print("It was manufactured in the year", self.year)

car = Car("Toyota", "Corolla", 2022)
car.describe()
