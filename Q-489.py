#  Write a function cust_data() to ask user to enter their names and age to store data in customer.txt file

def cust_data(name,age):
    f1=open("data.txt","a")
    f1.write("Name: ")
    f1.write(name)
    f1.write("\n")
    f1.write("Age: ")
    f1.write(age)
    f1.write("\n")
    f1.write("\n")
    f1.close()

ip=int(input("Enter How Much Data You Have To Enter ?: "))
for i in range (ip):
    nm=input("Enter Name: ")
    ag=input("Enter Age: ")
    cust_data(nm,ag)
