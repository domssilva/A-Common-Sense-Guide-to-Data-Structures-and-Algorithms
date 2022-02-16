# implement a min-heap
class minheap:
    def __init__(self):
        self.heap = []
    
    def insert(self, node):
        # insert node
        self.heap.append(node)
        # restore heap property
        if len(self.heap) > 1:
            self.trickle_up()

    def trickle_up(self):
        new_node_idx = len(self.heap)-1
        parent_node_idx = self.parent_idx(new_node_idx)
        while self.heap[new_node_idx] < self.heap[parent_node_idx]:
            self.swap(new_node_idx, parent_node_idx)
            new_node_idx = parent_node_idx
            parent_node_idx = self.parent_idx(new_node_idx)

    def trickle_down(self):
        # starting from the root
        node_idx = 0
        # if smaller child, keep swapping
        while self.has_smaller_child(node_idx):
            child_idx = self.get_smaller_child_idx(node_idx)
            self.swap(node_idx, child_idx)
            node_idx = child_idx

    def get_smaller_child_idx(self, idx):
        left = self.left_child_idx(idx)
        right = self.right_child_idx(idx)
        if self.heap[left] < self.heap[right]:
            return left
        return right

    def has_smaller_child(self, idx):
        left = self.left_child_idx(idx)
        right = self.right_child_idx(idx)
        # check if indexes are in range to avoid an exception
        if left < len(self.heap) and right < len(self.heap):
            return (
                (self.heap[left] and self.heap[left] < self.heap[idx]) or 
                (self.heap[right] and self.heap[right] < self.heap[idx])
                )
        return False

    def search(self, node):
        pass

    def delete(self):
        # place last node as root
        self.heap[0] = self.heap[-1]
        # delete last node's old location
        self.heap.pop()
        # restore heap
        self.trickle_down()

    def swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def get_root(self):
        return self.heap[0]

    def get_last_node(self):
        return self.heap[-1]

    def left_child_idx(self, idx):
        return 2*idx + 1
    
    def right_child_idx(self, idx):
        return 2*idx + 2

    def parent_idx(self, idx):
        return int((idx-1)/2)


heap = minheap()
heap.insert(10)
heap.insert(30)
heap.insert(15)
heap.insert(35)
heap.insert(32)
heap.insert(31)
heap.insert(20)
# [10, 30, 15, 2, 32, 31, 20, 35]

heap.insert(2)
# [2, 10, 15, 30, 32, 31, 20, 35]

# [10, 30, 15, 2, 32, 31, 20, 35]
heap.delete()

print(heap.heap)