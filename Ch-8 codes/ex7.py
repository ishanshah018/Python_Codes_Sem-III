# Custom Exception

def add(a,b):
    if type(a)==str:
        raise TypeError("a should be int")
    if type(b)==str:
        raise TypeError("b should be int")
    