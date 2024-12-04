#  Write a Python program using function to shift the decimal digits n places to the left, wrapping the extra digits around. If 
# shift > the number of digits of n, then reverse the string.
#  Note: 
# Function will take two parameters: 
# 1. The number 
# 2. How much shift user want
#  Example:
#  Input: n=12345 shift=1
#  Output: Result=23451
#  Input: n=12345 shift=3
#  Output: Result=45123
#  Input: n=12345 shift=5
#  Output: Result=12345
#  Input: n=12345 shift=6
#  Output: Result=54321

n = int(input("Enter Number: "))
s = int(input("Enter Shifting: "))

str_n = str(n)
if s > len(str_n):
    result = str_n[::-1]
else:
    result = str_n[s:] + str_n[:s]

print(result)
