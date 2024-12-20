# Custom Exception

def add(a,b):
    if type(a)==str:
        raise TypeError("a should be int")
    if type(b)==str:
        raise TypeError("b should be int")
      
# --------------------------------------------------
# Custom Exception with Class name

class NotValidAge(Exception):
    def __str__(self):
        return 'Age Should be greater than 18 years !!'

def driving_licence(age):
    if age<18:
        raise NotValidAge
    
driving_licence(12)
# ---------------------------------------------------
# Custom Exception with Class name with try,except

class NotValidAge(Exception):
    def __str__(self):
        return 'Age Should be greater than 18 years !!'

def driving_licence(age):
    try:
        if age<18:
            raise NotValidAge
    except Exception as e:
        print(e)
    
driving_licence(12)
