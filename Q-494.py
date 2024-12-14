#  Write a python program that reads a text file and changes the file by capitalizing each character of file.

with open("city.txt", 'r') as f1:  
      lines = f1.readlines()

with open("city.txt", 'w') as f2:  
    for line in lines:
        f2.write(line.upper())  

print("File has been capitalized.")
