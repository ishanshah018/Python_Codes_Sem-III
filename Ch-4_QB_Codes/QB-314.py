#  Write a program to calculate the sum and average of the digits present in a string.

s=input("Enter String: ")
sum_digits = 0
count = 0

for c in s:
    if c.isdigit():
        sum_digits += int(c)
        count += 1

print("Sum:", sum_digits)
print("Average:", sum_digits / count)