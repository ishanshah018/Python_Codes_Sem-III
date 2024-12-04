#  Write a Python program to return another string similar to the input string, but with its case inverted. 
# For example, input of “Mr. Ed” will result in “mR. eD” as the output string.
#  Note: Use of built in swapcase function is prohibited

s=input("Enter String: ")
result=""

for char in s:
    if char.isupper():
        result += char.lower()
    elif char.islower():
        result += char.upper()
    else:
        result += char
print(result)