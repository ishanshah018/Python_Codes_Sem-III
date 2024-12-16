# Getters & Setters

class Library:
    def __init__(self,id,name):
        self.bookid=id
        self.bookname=name
    
    def setbookname(self,newname):
        self.bookname=newname
    
    def getbookname(self):
       print("Name of Book is: ",self.bookname)

b=Library(1,"Witchers") 
b.getbookname()

b.setbookname("Harry Porters")
b.getbookname()