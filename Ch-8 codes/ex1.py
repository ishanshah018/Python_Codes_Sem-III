class Home:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def speak(self):
        print("I can speak ",self.name)
        
    def eat(self,fav_dish):
        print("I love to Eat",fav_dish)
        
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
x=Home("Ishan",19)
print(x.name)
x.display()
x.speak()
x.eat()