# WAP to make a list by running through elements of list and adding all elements greater than itself.
# i/p:- [2,4,6,10,1]
# o/p:- [22,20,16,10,23]

l=[2,4,6,10,1]
result=[]
for i in l:
    sum=0
    for j in l:
        if j>=i:
            sum=sum+j
    result.append(sum)
print(result)