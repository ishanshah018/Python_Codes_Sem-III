#  Write a python program to read a text file “Story.txt” and print only word starting with ‘I’ in reverse order.
#  Example: If value in text file is : ‘INDIA IS MY COUNTRY’
#  Output will be: ‘AIDNI SI MY COUNTRY’

with open("words.txt","r") as f:
    data=f.read().split()
    for i in data:
        if i[0]=="I":
            rev=i[::-1]
            print(rev,end=' ')
        else:
            print(i,end=' ')
