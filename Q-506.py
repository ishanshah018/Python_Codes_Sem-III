#  Write a python program to accept string/sentence from user till the user enters “END”. Each string/sentence entered by 
# user should be a newline in file. Save all the lines in file and display only those lines which begin with capital letter.
#  Example:
#  Enter Something (for quit enter END):Hi Friends
#  Enter Something (for quit enter END):how are you all
#  Enter Something (for quit enter END):I am fine
#  Enter Something (for quit enter END):hope you all are fine
#  Enter Something (for quit enter END):END

#  o/p:
#  The Line started with Capital Letters:
#  Hi Friends
#  I am fine

f1 = open("file1.txt", "w")

n = True
while n:
    x = input("Enter Something (for quit enter END): ")
    if x == "END":
        n = False
    else:
        f1.write(x + "\n") 

f1.close() 

with open("file1.txt", "r") as f2:
    data = f2.readlines() 
    print("The Lines started with Capital Letters:")
    for line in data:
        line = line.strip()  # Remove any leading/trailing whitespaces or newlines
        if line and line[0].isupper():  # Check if the line starts with an uppercase letter
            print(line)  # Print the valid line

f2.close()
