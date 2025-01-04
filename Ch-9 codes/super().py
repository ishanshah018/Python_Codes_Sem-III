class Company:
    def company_name(self):
        return "Google"

class Employee(Company):
    def emp_info(self):
        c_name=super().company_name()
        print("Ishan Works at: ",c_name)
        
emp=Employee()
emp.emp_info()