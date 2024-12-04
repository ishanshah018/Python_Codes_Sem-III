# Write a program to find all occuences of a sub string in a given string by ignoring the case

s = input("Enter the String you want to search:")
sub = input("Enter the Sub-String you want to search:")
count = 0
a = s.lower().split() 
sub = sub.lower()

for i in a:
    if sub in i: 
        count += 1

print("Total Occurrence of", sub, "is:", count)
