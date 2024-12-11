#  Write a Python program to read a text file and do following: 1. Print no. of words 2. Print no. statements 

f = open("city.txt", "r")
content = f.read()
word_count = len(content.split())
print(word_count)
