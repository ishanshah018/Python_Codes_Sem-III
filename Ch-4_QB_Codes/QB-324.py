#  Write a program to print sum of even numbers and sum of odd numbers from elements given in tuple.

t = (1, 2, 3, 4)
even_sum = 0
odd_sum = 0

for n in t:
    if n % 2 == 0:
        even_sum += n
    else:
        odd_sum += n

print("Even Sum:", even_sum)
print("Odd Sum:", odd_sum)