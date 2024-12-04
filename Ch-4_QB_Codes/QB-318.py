#  Write a Python program to capitalize the first and last character of each word in a string

s=input("Enter String: ")
a=s.split()
for word in a:
    print(word[0].upper() + word[1:-1] + word[-1].upper(), end=" ")
