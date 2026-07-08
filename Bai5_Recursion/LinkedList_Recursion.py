class SingleNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

# Time: O(n), Space: O(n)
def reverse_linked_list(node):
    if not node:
        return

    reverse_linked_list(node.next)
    print(node)

if __name__ == '__main__':
    Head = SingleNode(1)
    A = SingleNode(2)
    B = SingleNode(3)
    C = SingleNode(4)

    Head.next = A
    A.next = B
    B.next = C

    reverse_linked_list(Head)