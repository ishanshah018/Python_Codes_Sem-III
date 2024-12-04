# Write a program to create a string made of first,middle and last character

s=input("Enter String: ")
l=len(s)
res=s[0]+s[l//2]+s[-1]
print(res)