# Write a function count_lines() to count and display the total number of lines from the file. Consider the following lines for 
# the file – friends.txt.
# Friends are crazy, Friends are naughty !
# Friends are honest, Friends are  best !
# Friends are like keygen, friends are like license key !
# We are nothing without friends, Life is not possible without friends !

f1=open("friends.txt","w")
f1.write('''Friends are crazy, Friends are naughty !
Friends are honest, Friends are  best !
Friends are like keygen, friends are like license key !
We are nothing without friends, Life is not possible without friends !''')

f1.close()

f1=open("friends.txt","r")

def count_lines():
    ln=f1.readlines()
    l=len(ln)
    print(l)
    
count_lines()
