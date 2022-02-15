class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0

    def read(self, idx):
        current_idx = 0
        current_node = self.head
        if idx >= 0:
            while current_node and current_idx < idx:
                current_idx+=1
                current_node = current_node.next
            return current_node.data

    def insert(self, data, idx):
        # insert the head
        new_node = Node(data)
        if idx == 0:
            if self.head:
                new_node.next = self.head.next
            self.head = new_node
        else:
            # anywhere else
            previous_node = self.get_previous(idx)
            new_node.next = previous_node.next
            previous_node.next = new_node
        self.size += 1

    # returns index of node. if not found, returns -1
    def search(self, data):
        node = self.head
        current_idx = 0
        while node:
            if node.data == data:
                return current_idx
            node = node.next
            current_idx += 1
        return -1

    # find node at idx-1
    def get_previous(self, idx):
        node = self.head
        current_idx = 0
        while node and current_idx < idx-1:
            node = node.next
            current_idx += 1
        return node

    def delete(self, idx):
        # head
        if idx == 0:
            self.head = self.head.next
        else:
            # any other node
            previous_node = self.get_previous(idx)
            node_to_delete = previous_node.next
            previous_node.next = node_to_delete.next
        self.size -= 1

    def traverse(self, node):
        if not node:
            return node
        print(node.data)
        self.traverse(node.next)


linkedlist = Linkedlist()
linkedlist.insert(5, 0)
linkedlist.insert(2, 1)
linkedlist.insert(7,2)
linkedlist.insert(1,3)
#linkedlist.delete(3)
# print(linkedlist.read(2))

print(linkedlist.search(5))

#linkedlist.traverse(linkedlist.head)