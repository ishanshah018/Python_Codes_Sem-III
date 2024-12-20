def div(a,b):
    return a/b
try:
    print(div(6,3))
except:
    print("Exception occured")
else:
    print("No any Exceptions !!")
finally:
    print("Runs every time..")
