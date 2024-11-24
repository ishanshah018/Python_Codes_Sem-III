# WAP to Convert a list of Tuples into Dictionary.
# i/p:- [("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]
# o/p:- {'akash': [10], 'gaurav': [12], 'anand': [14], 'suraj': [20], 'akhil': [25], 'ashish': [30]}

# Example 2:

# i/p:- [('A', 1), ('B', 2), ('C', 3)]
# o/p:- {'A': [1], 'B': [2], 'C': [3]}

list=[("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]
dict={}
for i,j in list:
    dict[i]=j
print(dict)