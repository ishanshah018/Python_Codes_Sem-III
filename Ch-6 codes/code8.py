# # WAP to read lines from file1 and file2, write one line from each alternately into file3, and add remaining lines at the end

f1 = open("file1.txt", "w")
f2 = open("file2.txt", "w")

list1 = ["1\n", "2\n", "3\n", "4\n", "5\n", "6\n", "7\n", "8\n", "9\n", "10\n"]
list2 = ["A\n", "B\n", "C\n", "D\n", "E\n", "F\n"] 

f1.writelines(list1)
f2.writelines(list2)
f1.close()
f2.close()

with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("file3.txt", "w") as f3:
    for line1, line2 in zip(f1, f2):
        f3.write(line1)
        f3.write(line2)
    f3.writelines(f1)  
    f3.writelines(f2)  
