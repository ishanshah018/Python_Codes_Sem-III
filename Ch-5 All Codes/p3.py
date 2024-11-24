# List Comprehension Codes:

# Scalar Multiplication on Vector

v=[2,3,4]
s=2
print([s*i for i in v])

# Print all numbers divisible by 5 in range 1 to 50
print([i for i in range(1,51) if i%5==0])

# find languages which starts with p
# lang=['java','python','php','c','jas=vascript']

lang=['java','python','php','c','jas=vascript']
print([language for language in lang if language.startswith('p')])

# Print a (3,3) Matrix using Nested List Comprehension
print([[i*j for i in range(1,4)]for j in range(1,4)])

# Cartesian Products
l1=[1,2,3,4]
l2=[5,6,7,8]
print([i*j for i in l1 for j in l2])