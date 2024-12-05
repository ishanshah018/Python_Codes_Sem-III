# Write a Python program to rearrange the elements of a list L of size n in the order:

# L[0], L[n-1], L[1], L[n-2], L[2], L[n-3], ...

# Input:
# A list L containing n elements.

# Output:
# A new list with elements rearranged in the specified order.

# Examples:
# Input: L = [10, 20, 30, 40]
# Output: [10, 40, 20, 30]

# Input: L = [1, 2, 3, 4, 5]
# Output: [1, 5, 2, 4, 3]

# Input: L = [7, 14, 21, 28]
# Output: [7, 28, 14, 21]

# Input: L = [100]
# Output: [100]



L = eval(input("Enter List: "))
n = len(L)
output = []

# Rearrange elements
for i in range((n + 1) // 2):
    output.append(L[i])           # Front element
    if i != n - 1 - i:            # Avoid duplicate middle element for odd-sized lists
        output.append(L[n - 1 - i])  # Back element

# Print the result
print(output)
