#  WAP to read lines from file1 and file2, write one line from each alternately into file3, and add remaining lines at the end

with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("file3.txt", "w") as f3:
    for line1, line2 in zip(f1, f2):
        f3.write(line1)
        f3.write(line2)
    f3.writelines(f1)  
    f3.writelines(f2) 
