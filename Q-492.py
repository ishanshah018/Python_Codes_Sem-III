#  Write a function display_oddLines() to display odd number lines from the text file. Consider the following lines for the file – 
# friends.txt.
#  Friends are crazy, Friends are naughty !
#  Friends are honest, Friends are  best !
#  Friends are like keygen, friends are like license key !
#  We are nothing without friends, Life is not possible without friends !

f1=open("friends.txt","w")
f1.write('''Friends are crazy, Friends are naughty !
Friends are honest, Friends are  best !
Friends are like keygen, friends are like license key !
We are nothing without friends, Life is not possible without friends !''')

f1.close()

def display_oddLines():
    with open('friends.txt', 'r') as file:
        line_number = 1
        
        for line in file:
            if line_number % 2 != 0:
                print(line, end='') 
            line_number += 1
display_oddLines()
