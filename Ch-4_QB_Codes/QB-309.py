#  Write a Python function that accepts a string and calculate the number of uppercase letters and lowercase letters

s=input("Enter String: ")
up=0
lo=0
for i in s:
    if i.isupper():
        up+=1
    elif i.islower():
        lo+=1
print("Total Number of Upper Case Words are: ",up)
print("Total Number of Lower Case Words are: ",lo)