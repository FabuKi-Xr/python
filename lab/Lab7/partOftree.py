class Node():
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)

class BST():
    def __init__(self) -> None:
        self.root = None
    def insert(self,data):
        newNode = Node(data)
        node = self.root
        if self.root == None:
            self.root = newNode
        else:
            while True:
                if node != None:
                    if node.data < data:
                        if node.right == None:
                            node.right = newNode
                            return self.root
                        else:
                            node = node.right
                    else:
                        if node.left == None:
                            node.left = newNode
                            return self.root
                        else:
                            node = node.left
        return self.root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def checkpos(self,data):
        node = self.root
        while True:
            if node != None:
                if node.data == data:
                    if node == self.root:
                        print("Root")
                    elif node.left == node.right == None:
                        print("Leaf")
                    elif node.left != None or node.right != None:
                        print("Inner")
                    return
                else:
                    if node.data < data:
                        node = node.right
                    else:
                        node = node.left
            else:
                print("Not exist")
                return

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1,len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
T.checkpos(inp[0])