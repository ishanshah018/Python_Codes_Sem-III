#  Write a python program to search for a string in text files.

filename = input("Enter the name of the file: ")
search_string = input("Enter the string to search for: ")

with open(filename, 'r') as f:
  for line in f:
    if search_string in line:
      print("Found :", line.strip())
