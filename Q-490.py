#  Write a python program to create and read the city.txt file in one go and print the contents on the output screen.

f1=open("city.txt","a")
f1.write("Ahmedabad\n")
f1.write("Vadodara\n")
f1.write("Surat\n")
f1.write("Jamnagar\n")
f1.write("Rajkot\n")
f1.close()

f1=open("city.txt","r")
data=f1.read()
print(data)
