class test:
    def __init__(self,a="Hello World"):
        self.a=a
    def display(self):
        print(self.a)
obj=test()
obj.display()

obj2=test("Change")
obj2.display()