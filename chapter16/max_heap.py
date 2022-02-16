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

    def delete(self):
            # Remove last element of heap and place it as the new root
            self.data[0] = self.data.pop()
            # trickle node down
            trickle_node_idx = 0
            while self.has_greater_child(trickle_node_idx):
                # save larger child index in variable
                larger_child_idx = self.calculate_larger_child_idx(trickle_node_idx)
                self.swap(trickle_node_idx, larger_child_idx)
                trickle_node_idx = larger_child_idx

    def has_greater_child(self, idx):
        left = self.left_child_idx(idx)
        right = self.right_child_idx(idx)
        # check if indexes are in range to avoid an exception
        if left < len(self.data) and right < len(self.data):
            return (
                (self.data[left] and self.data[left] > self.data[idx]) or 
                (self.data[right] and self.data[right] > self.data[idx])
                )
        return False

    def calculate_larger_child_idx(self, idx):
        # if there is no right child
        if not self.data[self.right_child_idx(idx)]:
            return self.left_child_idx(idx)
        # if right child is greater than left child
        if self.data[self.right_child_idx(idx)] > self.data[self.left_child_idx(idx)]:
            return self.right_child_idx(idx)
        # if left child is greater than or equal to right child
        else:
            return self.left_child_idx(idx)


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

heap.delete()
print('root:', heap.get_root())
print('last node:', heap.get_last())