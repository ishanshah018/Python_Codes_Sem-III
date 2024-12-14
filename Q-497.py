#  Write python program to count the number of lines in a file

f1=open("city.txt","r")
count=0
data=f1.readlines()
for i in data:
    count+=1
print(count)
