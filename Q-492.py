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
        lines = file.readlines() 
        for index, line in enumerate(lines):  # Enumerate through lines with their indices
            if (index + 1) % 2 != 0:  # Check if the line number is odd (index + 1)
                print(line, end='') 
display_oddLines()
