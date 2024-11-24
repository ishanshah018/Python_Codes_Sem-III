# WAP to add items of 2 lists indexwise
l1=[1,2,3,4]
l2=[5,6,7,8]

print([i+j for i,j in zip(l1,l2)])