#  File Filtering. write all lines of a file1, except those that start with a pound sign ( # ), the comment character for Python to  
#  file2. And display data of file2.
#  Text file1 content:
#  Friends are crazy, Friends are naughty ! 
#  #Friends are honest, Friends are best ! 
#  Friends are like keygen, #friends are like license key ! 
#  We are nothing without friends, Life is not possible without friends !

#  Text file2 shoud be:
#  Friends are crazy, Friends are naughty !  
#  Friends are like keygen, 
#  We are nothing without friends, Life is not possible without friends 

# WAP to remove '#' sign from the text 
f1=open("file1.txt","r")
f2=open("file2.txt","w")

for d in f1:  
    if d.startswith("#"): 
        continue
    if "#" in d:  
        d = d.split("#")[0].rstrip()  
    f2.write(d + "\n") 
f1.close()
f2.close()
