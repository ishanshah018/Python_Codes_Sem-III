#  Write a Python program to print even length words in a string

s=input("Enter String: ")
for word in s.split():
    if len(word) % 2 == 0:
        print(word)