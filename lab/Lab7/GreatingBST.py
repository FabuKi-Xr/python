class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
    def insert(self, data):
        newNode = Node(data)
        if self.root == None:
            self.root = newNode
        else:
            r = self.root
            while True:
                if data < r.data :
                   if r.left == None:
                       r.left = newNode
                       break
                   r = r.left
                else:
                    if r.right == None:
                        r.right = newNode
                        break
                    r = r.right
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)