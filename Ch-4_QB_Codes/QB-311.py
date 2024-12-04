# Write a program to remove I'th character from string in python 

s = input("Enter the string: ")
i = int(input("Enter the index of the character to remove: "))
result = s[:i] + s[i+1:]
print("String after removal:", result)
