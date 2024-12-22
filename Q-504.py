#  Write a Python program to count words, characters and spaces from text file.

#  Input:
#  Python is a Easy SubjectOOPs is One of the most interesting Topic

#  Output:
#  No of space: 11
#  No of word: 12
#  No of character: 65

f=open("file1.txt","r")
data=f.read()

char_count=0
word_count=0
space_count=0

for i in data:
    char_count+=1
    if i==" ":
        space_count+=1

word_count=len(data.split())

print("No of space: ",space_count)
print("No of word: ",word_count)
print("No of character: ",char_count)
f.close()
