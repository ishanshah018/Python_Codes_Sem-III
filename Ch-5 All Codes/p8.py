#  WAP to sort a list of alphanumeric strings based on product value of numeric elements in it.
#  Note:[If there are no numeric element present in that string take its product value=1]
#  i/p:- l=['1ac21','23fg','456','098d','1','kls']
#  o/p:- ['456','23fg','lac21','kls','1',''098d]

l=['1ac21','23fg','456','098d','1','kls']
prod_val=[]
for item in l:   #here one by one string cames 1st:'1ac21' 2nd:'23fg' and ...
    product=1
    for char in item: #here the splitting of each words of particular strings takes place
        
       if char.isdigit():
           product=product*int(char)
    prod_val.append(product)
# print(prod_val)
print([i[1] for i in sorted(list(zip(prod_val,l)),reverse=True)])