# catching specific exception 
try:
 m=5 
 f = open('sample1.txt','r')
 print(f.read())
 print(m)
 print(5/2)
 L = [1,2,3]
 L[100] 

except FileNotFoundError:
   print('file not found')
except NameError:
   print('variable not defined')
except ZeroDivisionError:
   print("can't divide by 0")
except Exception as e:
   print(e)
