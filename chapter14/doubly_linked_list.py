class Node:
    def __init__(self, data, previous=None, next=None):
        self.data = data
        self.previous = previous
        self.next = next


class Doublylinkedlist:
    def __init__(self):
        self.head = None # first node
        self.tail = None # last node

    # push value at the end of the list
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            # insert first node
            self.head = new_node
            self.tail = new_node
        else:
            # assign links
            new_node.previous = self.tail
            self.tail.next = new_node
            # update tail with new node
            self.tail = new_node

    def traverse(self, node):
        if not node:
            return
        print(node.data, end=' ')
        self.traverse(node.next)

    def reverse(self, node):
        if not node:
            return
        print(node.data, end=' ')
        self.reverse(node.previous)

    
dlist = Doublylinkedlist()

dlist.insert(3)
dlist.insert(2)
dlist.insert(1)

print('traverse:')
dlist.traverse(dlist.head)
print('\nreverse:')
dlist.reverse(dlist.tail)
