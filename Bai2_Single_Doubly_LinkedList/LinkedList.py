# Singly Linked List
class SingleNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

# Display Singly Linked List
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print('->'.join(elements))

# Search for node value - O(n)
def search(head, val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next
    return False

# Doubly Linked List
class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)

# Display Linked List - O(n)
def displayDoubly(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print('<->'.join(elements))

# Insert at beginning - O(1)
def insert_at_beginning(head, tail, val):
    new_node = DoublyNode(val, next=head)
    head.prev = new_node
    return new_node, tail

# Insert at end - O(1)
def insert_at_end(head, tail, val):
    new_node = DoublyNode(val, prev=tail)
    tail.next = new_node
    return head, new_node

if __name__ == '__main__':
    # Singly Linked List
    Head = SingleNode(1)
    A = SingleNode(3)
    B = SingleNode(4)
    C = SingleNode(7)

    Head.next = A
    A.next = B
    B.next = C

    # Traverse the list (Duyệt linkedList) - O(n)
    display(Head)

    # Search value in LinkedList
    print(search(Head, 3))
    print("========================================")

    # Doubly Linked List
    head = tail = DoublyNode(1)

    # Insert at beginning
    head, tail =  insert_at_beginning(head, tail, 3)
    displayDoubly(head)

    # Insert at end
    head, tail = insert_at_end(head, tail, 7)
    displayDoubly(head)
