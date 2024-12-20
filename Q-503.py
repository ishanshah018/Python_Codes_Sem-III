#  Write a python program to read a text file “Story.txt” and print only word starting with ‘I’ in reverse order.
#  Example: If value in text file is : ‘INDIA IS MY COUNTRY’
#  Output will be: ‘AIDNI SI MY COUNTRY’

with open("file1.txt", "r") as f:
    data = f.read()
    lines = data.splitlines()
    for line in lines:
        words = line.split()
        for w in words:
            if w[0] == 'I':
                print(w[::-1], end=" ")
            else:
                print(w, end=" ")
