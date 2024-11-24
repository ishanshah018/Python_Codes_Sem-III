#  WAP to Convert List to List of Dictionaries. List: Keys & values , Convert that list to dictionary distributing key from key list to values
#  i/p:- l=["DataScience",3,"is",8] key_list=["name","id"]
#  o/p:- [{',{'name':'Data-Science','id':3},{name':'is','id':8}]

#  Example 2:

#  i/p:- l=['CampusX',10] key_list=['name','id']
#  o/p:- [{'name':'CampusX','id':10}]

l=["DataScience",3,"is",8] 
key_list=["name","id"]
result = []

# Iterate over the test_list in chunks of size equal to the key_list
for i in range(0, len(l), len(key_list)):
    # Zip the chunk with the key_list and convert to dictionary
    temp_dict = dict(zip(key_list, l[i:i+len(key_list)]))
    result.append(temp_dict)

print(result)