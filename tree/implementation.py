class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
    
    def printTree(self):
        print(self.data)
        print(self.left)
        print(self.right)


root = Node(27)
# root.left = Node(25)
# root.right = Node(30)
root.printTree()

# inorder traversal (left, root, right)
# 4 2 5 1 3 6 7
# pre order travrersal (root, left, right)
# 1 2 4 5 3 6 7
# post order traversal (right,left, root)


