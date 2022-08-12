# Doubly Linked List Implementation


# Node class
from hashlib import new


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)

# Doubly Linked List class


class DoublyLinkedList:
    # Constructor for an empty doubly linked list
    def __init__(self):
        self.head = None
        self.tail = None

    # Given a reference to the head of a list and an
    # integer, inserts a new node on the front of list

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.prev = None
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    # Given a node as prev_node, insert
    # a new node after the given node

    def insertAfter(self, prev_node, new_data):
        new_node = Node(new_data)
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next = new_node
        if new_node.next is not None:
            new_node.next.prev = new_node

    # Add a node at the end of the Doubly linked list

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def printList(self, node):
        while node:
            print(" {}".format(node.data))
            node = node.next


llist = DoublyLinkedList()

# Insert 6. So the list becomes 6->None
llist.append(6)

# Insert 7 at the beginning.
# So linked list becomes 7->6->None
llist.push(7)

# Insert 1 at the beginning.
# So linked list becomes 1->7->6->None
llist.push(1)

# Insert 4 at the end.
# So linked list becomes 1->7->6->4->None
llist.append(4)

# Insert 8, after 7.
# So linked list becomes 1->7->8->6->4->None
llist.insertAfter(llist.head.next, 8)

print("Created DLL is: ")
llist.printList(llist.head)


llist1 = DoublyLinkedList()

# Insert 5. So the list becomes 5->None
llist1.append(5)

# Insert 2 at the beginning.
# So linked list becomes 2->5->None
llist1.push(2)

# Insert 3 at the beginning.
# So linked list becomes 3->2->5->None
llist1.push(3)

# Insert 8, after 5.
# So linked list becomes 3->2->5->8->None
llist1.insertAfter(llist1.head.next.next, 8)

print("Created DLL is: ")
llist1.printList(llist1.head)