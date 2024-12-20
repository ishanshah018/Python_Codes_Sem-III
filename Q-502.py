# Write a python program to extract a list of all four-letter words that start and end with the same letter from a given text file

with open("file1.txt", "r") as f:
    data = f.read()  
    for line in data.splitlines():  
        words = line.split()  
        for i in words:
            if len(i) == 4 and i[0].lower() == i[-1].lower():
                print(i)
