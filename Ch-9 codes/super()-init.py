class Company:
    def __init__(self):
        self.id=12
        self.name="Ishan"
    def comp_name(self):
        return "Google"
    
class Employee(Company):
    def __init__(self):
        super().__init__()
        self.n=111
    def info(self):
        print("Ishan works at")
    
emp=Employee()
emp.info()
print(emp.name)
print(emp.comp_name())

print(issubclass(Employee,Company))