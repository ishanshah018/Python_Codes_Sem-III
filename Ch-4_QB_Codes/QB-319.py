#  Write a program to Create a string made of the middle three characters

s=input("Enter String: ")
if len(s) >= 3 and len(s) % 2 != 0:
    mid = len(s) // 2
    print(s[mid - 1:mid + 2])
else:
    print("The string must have an odd length and at least 3 characters.")