# WAP to print a list after performing running sum on it.
# i/p:- [1,2,3,4,5,6]
# o/p:- [1,3,6,10,15,21]

list=[1,2,3,4,5,6]
result=[]
sum=0
for i in list:
    sum=sum+i
    result.append(sum)
print(result)