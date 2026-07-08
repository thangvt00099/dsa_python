# Create Array/List
A = [1, 2, 3]
print(A)

# Append - Insert element at end of array - O(1)
A.append(5)
print(A)

# Pop - Delete element at end of array - O(1)
A.pop()
print(A)

# Insert (not at end of array) - O(n)
A.insert(2, 5)
print(A)

# Modify an element - O(1)
A[0] = 7
print(A)

# Accessing element given index i - O(1)
print(A[2])

# Check if element exists - O(n)
if 6 in A:
    print("YES")
else: print("NO")

# Size of array - O(1)
print(len(A))
print("=============")

# Strings
s = "Hello"

# Append to end of string - O(n)
b = s + "z"
print(b)

# Check if something is in string
if "e" in b:
    print("YES")
else: print("NO")

# Access positions - O(1)
print(s[2])
