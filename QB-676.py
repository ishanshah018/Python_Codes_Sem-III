class Book:
    def __init__(self,pages):
        self.pages=pages
        
    def __add__(self,other):
        return Book(self.pages+other.pages)
    
d1=Book(100)
d2=Book(200)
d3=Book(300)
t=d1+d2+d3
print(t.pages)
