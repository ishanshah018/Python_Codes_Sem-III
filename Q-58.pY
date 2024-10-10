# Write a Python program to calculate surface volume and area of a cylinder.
import math

print("For Calculating Volume and Surface Area of Cylinder : ")

r=int(input("Enter Radius: "))
h=int(input("Enter Height: "))
v=math.pi*r*r*h;
sa=(2*math.pi*r*h)+(2*math.pi*r*r)
print("Volume of Cylinder is: ",v)
print("Surface Area of Cylinder is: ",sa)


