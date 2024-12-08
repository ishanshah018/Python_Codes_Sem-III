# To read all lines into list

f=open("test.txt","r")
lines=f.readlines()
for i in lines:
    print(i,end="")
f.close()