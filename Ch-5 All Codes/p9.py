# WAP that Splits String of list on K character
#  i/p:- l=['CampusX is a channel','for data-science','aspirants.']
#  o/p:- ['CampusX','is','a','channel','for','data-science','aspirants']
l=['CampusX is a channel','for data-science','aspirants.']
result=[]
for i in l:
    result.extend(i.split())
print(result)

