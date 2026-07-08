# Stacks - Last In First Out
stk = []
print(stk)

# Append to top of stack - O(1)
stk.append(5)
stk.append(4)
stk.append(3)
print(stk)

# Pop from stack - O(1)
x = stk.pop()
print(x)
print(stk)

# Ask what's on the top of stack - O(1)
print(stk[-1])

# Ask if something is in the stack - O(1)
if stk:
    print(True)
print("====================")

# Queue - First In First Out (FIFO)
from collections import deque
q = deque()

# Add element to the right - O(1)
q.append(5)
q.append(6)
q.append(7)
print(q)

# Remove element to the left - O(1)
q.popleft()
print(q)

# Peek from left side - O(1)
print(q[0])

# Peek from right side - O(1)
print(q[-1])