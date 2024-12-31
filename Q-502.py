# Write a python program to extract a list of all four-letter words that start and end with the same letter from a given text file

with open("file.txt", "r") as f:
    for word in f.read().split():
        if len(word) == 4 and word[0].lower() == word[-1].lower():
                print(word)
