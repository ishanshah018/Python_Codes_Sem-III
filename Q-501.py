f=open("file.txt","r")
data=f.read()

# To Reverse the content aqnd store to a file
reversed_data=data[::-1]
with open("file_rev.txt","w") as t:
    t.write(reversed_data)
    
# To uppercase reversed content to a file 
up_case=reversed_data.upper()    
with open("file_rev_uper.txt","w") as t1:
    t1.write(up_case)
 
# To count No.of vowels in file   
vowels="aeiouAEIOU"
count=0
for line in reversed_data:
    if line in vowels:
        count+=1
print("No of Vowels: ",count)

# To Print second line of file
with open("file_rev_uper.txt","r") as t2:
    data2=t2.readlines()
    line2=data2[1].strip()
print(line2)
