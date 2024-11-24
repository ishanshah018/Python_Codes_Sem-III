# WAP to Sort Dictionary key and values List.
#  i/p:- {'c': [3], 'b': [12, 10], 'a': [19, 4]}
#  o/p:- {'a': [4, 19], 'b': [10, 12], 'c': [3]}
#  Example 2:
#  i/p:- {'c': [10, 34, 3]}
#  o/p:- {'c': [3, 10, 34]}

dict={'c': [3], 'b': [12, 10], 'a': [19, 4]}
result={}
for i in sorted(dict):
   result[i]=sorted(dict[i])
print(result)