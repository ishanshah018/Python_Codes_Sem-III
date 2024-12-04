# Write a Python programme that accepts a string and calculate the number of uppercase letters, lowercase letters and 
# number of digits.
# For example,
# Input: Hello Pyth@n is 100% easy
# Output:
# Uppercase letters : 2
# Lowercase letters : 14
# Digits : 3

s=input("Enter String: ")
up=0
lo=0
digit=0
for i in s:
    if i.isupper():
        up+=1
    elif i.islower():
        lo+=1
    elif i.isdigit():
        digit+=1
print("Uppercase letters: ",up)
print("Lowercase letters: ",lo)
print("Digits: ",digit)