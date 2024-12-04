#  Write a Python program to  Uppercase Half String from the given string.

s=input("Enter String: ")
half = len(s) // 2
print(s[:half] + s[half:].upper())