#Write a python program to convert fahrenheit to celcius and vice versa.

f=float(input("Enter Temperature in Farenheit: "))
c=(f-32)*(5/9)
print("Temperature in Celsius is: ",c)

cel=float(input("Enter Temperature in Celsius: "))
fr=((9/5)*cel)+32
print("Temperature in Farenheit is: ",fr)

