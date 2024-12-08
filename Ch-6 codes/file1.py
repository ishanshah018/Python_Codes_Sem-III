f=open("test.txt","w")
f.write("This is Testing1")
print("File Name: ",f.name)
print("File Mode: ",f.mode)
print("Readable: ",f.readable())
print("Writable: ",f.writable())
print("Is File Closed ?: ",f.closed)

f.write("This is Testing2\n")
f.write("This is Testing3\n")

list=["Sunny\n","bunny\n","vinny"]
f.writelines(list)

f=open("test.txt","r")
data=f.read()
print(data)
f.close()
print("Is File Closed ?: ",f.closed)