class Home:
    name="ABC"
    species="Homogeneous"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
x=Home("Ishan",19)
print(x.name)
print(Home.name)
x.display()

print(x.species)
print(Home.species)