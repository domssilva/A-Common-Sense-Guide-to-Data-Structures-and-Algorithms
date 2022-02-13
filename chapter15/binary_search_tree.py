class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Bst:
    def __init__(self, data):
        self.root = Node(data)

    def search(self, data, node):
        if node == None or node.data == data:
            return node
        if data > node.data:
            return self.search(data, node.right)
        else:
            return self.search(data, node.left)

    def insert(self, data, node):
        if node == None or node.data == data:
            return
        if data > node.data:
            if node.right != None:
                return self.insert(data, node.right)
            else:
                node.right = Node(data)
        else:
            if node.left != None:
                return self.insert(data, node.left)
            else:
                node.left = Node(data)

    def delete(self, data, node):
        #basecase
        if node is None:
            return None
        # search for the node's parent
        elif data < node.data:
            node.left = self.delete(data, node.left)
            return node
        elif data > node.data:
            node.right = self.delete(data, node.right)
            return node
        # get node's successor
        elif data == node.data:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.right = get_successor(node.right, node)
                return node

    # from the left subtree
    def get_successor(node, node_to_delete):
        if node.left:
            node.left = self.get_successor(node, node_to_delete)
            return node
        else:
            node_to_delete.data = node.data
            return node.right

    # traversals
    def preorder(self, node):
        if (node == None): return
        print(node.data)
        self.inorder(node.left)
        self.inorder(node.right)
    def inorder(self, node):
        if (node == None): return
        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)
    def postorder(self, node):
        if (node == None): return
        self.inorder(node.left)
        self.inorder(node.right)
        print(node.data)
        

# root
tree = Bst(100)
# 2nd lvl
tree.insert(125, tree.root)
tree.insert(75, tree.root)
# 3rd lvl
tree.insert(65, tree.root)
tree.insert(150, tree.root)
tree.insert(115, tree.root)
# 4th lvl
tree.insert(110, tree.root)
tree.insert(70, tree.root)
tree.insert(60, tree.root)
tree.insert(175, tree.root)
tree.insert(135, tree.root)

# tests
print('==================================')
print('search nodes')
print('search 5:', tree.search(5, tree.root))
print('search 2:', tree.search(2, tree.root))
print('search 150:', tree.search(150, tree.root))
print('search 75:', tree.search(75, tree.root))
print('==================================')
print('delete 75')
tree.delete(75, tree.root)
print('==================================')
print('inorder traversal:')
tree.inorder(tree.root)
print('==================================')
print('preorder traversal:')
tree.preorder(tree.root)
print('==================================')
print('postorder traversal:')
tree.postorder(tree.root)