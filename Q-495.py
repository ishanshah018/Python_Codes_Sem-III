#  Write a Python program to copy the contents of a file to another file.

with open("city.txt", 'r') as f1:  
      lines = f1.readlines()

with open("city_new.txt", 'w') as f2:  
    for line in lines:
        f2.write(line)
