def preOrder(node):
    if node == None:
        return
    print(node.data)
    preOrder(node.left)
    preOrder(node.right)

class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
    
    def printTree(self):
        print(self.data)
        print(self.left)
        print(self.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.right.left = Node(7)
root.right.right = Node(8)
root.right.right.left = Node(9)
root.right.right.right = Node(10)

preOrder(root)