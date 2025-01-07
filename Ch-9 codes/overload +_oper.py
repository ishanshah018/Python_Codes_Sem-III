class Book:
    def __init__(self,pages):
        self.pages=pages
        
    def __add__(self,other):
        return self.pages+other.pages
    
d1=Book(100)
d2=Book(200)
print(d1+d2)