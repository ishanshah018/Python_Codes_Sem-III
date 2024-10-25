n=int(input("Enter Number: "))
st=int(input("Enter Starting Range: "))
end=int(input("Enter Ending Range: "))

def range(n,st,end):
    if n>st and n<end:
        print(n," is in given range")
    else:
        print(n," is not in given range")       

range(n,st,end)
