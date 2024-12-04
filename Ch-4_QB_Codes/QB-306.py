#  Write a Python program to check if a string is palindrome or not

s=input("Enter String: ")
if(s==s[::-1]):
    print("Entered String is Palindrome")
else:
    print("Entered String is NOT Palindrome")