# Max-heap
class Binary_Heap:
    def __init__(self):
        # initialize heap as an empty array
        self.data = []
    
    def get_root(self):
        return self.data[0]
    
    def get_last(self):
        return self.data[-1]

    def left_child_idx(self, idx):
        return 2*idx + 1
    
    def right_child_idx(self, idx):
        return 2*idx + 2

    def parent_idx(self, idx):
        return int((idx-1)/2)

    def swap(self, idx1, idx2):
        self.data[idx1], self.data[idx2] = self.data[idx2], self.data[idx1]

    def insert(self, data):
        # insert data
        self.data.append(data)
        new_node_idx = len(self.data)-1
        # handle trickle node
        parent_idx = self.parent_idx(new_node_idx)
        while new_node_idx > 0 and self.data[new_node_idx] > self.data[parent_idx]:
            self.swap(new_node_idx, parent_idx)
            # update inserted node idx
            new_node_idx = self.parent_idx(new_node_idx)
            parent_idx = self.parent_idx(new_node_idx)
            

heap = Binary_Heap()
heap.insert(100)
heap.insert(88)
heap.insert(25)
heap.insert(87)
heap.insert(16)
heap.insert(8)
heap.insert(12)
heap.insert(86)
heap.insert(50)
heap.insert(2)
heap.insert(15)
heap.insert(3)
heap.insert(140)

print('root:', heap.get_root())
print('last node:', heap.get_last())
print('Data:', heap.data)