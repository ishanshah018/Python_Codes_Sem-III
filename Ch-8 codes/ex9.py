# Custom Exception with Class name

class NotValidAge(Exception):
    def __str__(self):
        return 'Age Should be greater than 18 years !!'

def driving_licence(age):
    if age<18:
        raise NotValidAge
    
driving_licence(12)