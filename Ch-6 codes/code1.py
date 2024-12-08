#  To Read only first 10 characters

f=open("test.txt","r")
data=f.read(10)
print(data)

data2=f.readline()
print(data2)
f.close()