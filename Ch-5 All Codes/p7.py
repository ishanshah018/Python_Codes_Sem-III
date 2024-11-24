# WAP to find list of coomon unique elements from two lists and show them in Increasing order.
#  i/p: l1=[23,45,67,78,89,34,67]
#       l2=[34,89,55,56,39,67,67]
#  o/p:- [34,67,89]

l1=[23,45,67,78,89,34,67]
l2=[34,89,55,56,39,67,67]
l3=[]
for i in l1:
    if i in l2:
        if i not in l3:
            l3.append(i)
l3=sorted(l3)
print(l3)