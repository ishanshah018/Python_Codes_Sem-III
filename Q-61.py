#Write a python program to convert given days in to year, month and days.
days=int(input("Enter Days: "))
year=days//365
month=(days%365)//30
days=(days%365)%30
print(year," Years",month," Months",days," days")
