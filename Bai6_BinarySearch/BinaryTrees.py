# Binary Trees
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

# Recursive PreOrder (node-left-right) Traversal (DFS) Time: O(n), Space: O(n)
def pre_order(node):
    if not node:
        return

    print(node)
    pre_order(node.left)
    pre_order(node.right)

# Recursive InOrder (left-node-right) Traversal (DFS) Time: O(n), Space: O(n)
def in_order(node):
    if not node:
        return

    in_order(node.left)
    print(node)
    in_order(node.right)

# Recursive InOrder (left-node-right) Traversal (DFS) Time: O(n), Space: O(n)
def post_order(node):
    if not node:
        return

    post_order(node.left)
    post_order(node.right)
    print(node)

# Iterative PreOrder Traversal (DFS) Time: O(n), Space: O(n)
def pre_order_iterative(node):
    stk = [node]

    while stk:
        node = stk.pop()
        print(node)
        if node.right: stk.append(node.right)
        if node.left: stk.append(node.left)

# Level Order Traversal (BFS) Time: O(n), Space: O(n)
from collections import deque
def level_order(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)

# Check if value exists (DFS) Time: O(n), Space: O(n)
def search(node, target):
    if not node:
        return False

    if node.val == target:
        return True

    return search(node.left, target) or search(node.right, target)

# Binary Search Tree Time: O(logN), Space: O(logN)
def search_bst(node, target):
    if not node:
        return False

    if node.val == target:
        return True
    elif node.val < target:
        return search_bst(node.right, target)
    else: return search_bst(node.left, target)
if __name__ == '__main__':
    A = TreeNode(1)
    B = TreeNode(2)
    C = TreeNode(3)
    D = TreeNode(4)
    E = TreeNode(5)
    F = TreeNode(10)

    A.left = B
    A.right = C
    B.left = D
    B.right = E
    C.right = F

    print(pre_order(A))
    print("==============")
    print(in_order(A))
    print("==============")
    print(post_order(A))
    print("==============")
    print(pre_order_iterative(A))
    print("==============")
    print(level_order(A))
    print("==============")
    print(search(A, 3))
    print("==============")

    A2 = TreeNode(5)
    B2 = TreeNode(1)
    C2 = TreeNode(8)
    D2 = TreeNode(-1)
    E2 =  TreeNode(3)
    F2 = TreeNode(7)
    G2 = TreeNode(9)

    A2.left, A2.right = B2, C2
    B2.left, B2.right = D2, E2
    C2.left, C2.right = F2, G2

    print(in_order(A2))
    print("==============")
    print(search_bst(A2, 3))
