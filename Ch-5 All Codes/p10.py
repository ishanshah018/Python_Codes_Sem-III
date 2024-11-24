# WAP to Replace Words from Dictionary. Repace Given string from lookup Dictionary/
#  i/p:- test_str='CampusX best for DS students'
#        repl_dict={'best':'is the best channel',
#                   'DS':'Data-Science'}
#  o/p:- CampusX is  the best channel for Data-Science students

test_str='CampusX best for DS students'
repl_dict={'best':'is the best channel','DS':'Data-Science'}
result=[]

for i in test_str.split():
    if i in repl_dict:
        result.append(repl_dict[i])
    else:
        result.append(i)
print(" ".join(result))
