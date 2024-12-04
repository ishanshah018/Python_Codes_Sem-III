# Write a program to check if two strings are balanced. 
# For example, strings s1 and s2 are balanced if all the 
# characters in the s1 are present in s2 and length of s1 & s2 should be same. The character’s position doesn’t 
# matter.
#  Example :
#  s1 = hello
#  s2 = olleh
#  Balanced

s1 = input("Enter String-1: ")
s2 = input("Enter String-2: ")

if len(s1) != len(s2): 
    print("Strings are Not balanced")
elif sorted(s1) == sorted(s2):  # Check if characters and counts match
    print("Strings are balanced")
else:
    print("Strings are Not balanced")