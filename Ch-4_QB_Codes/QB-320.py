#  Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the 
# characters in the s1 are present in s2. The character’s position doesn’t matter

s1 = "abc"
s2 = "aabbcc"

for c in s1:
    if c not in s2:
        print("Strings are Not balanced")
        break
print("Strings are balanced")
