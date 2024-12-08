# WAP to count number of lines in a text file
c=0
f=open("test.txt","r")
for i in f:
    c+=1
print("Total Number of lines are: ",c)