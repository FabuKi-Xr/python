class Node():
    def __init__(self,data=None) -> None:
        self.data = data
        self.left = None
        self.right = None
    def __str__(self) -> str:
        return str(self.data)

class BST():
    def __init__(self) -> None:
        self.root = None
    def insert(self,node:Node,data):
        if self.root == None:
            print("*",end="")
            self.root = Node(data)
        else:
            if node != None:
                if node.data < data:
                    print("R",end="")
                    if node.right == None:
                        node.right = Node(data)
                        print("*",end="")
                        return
                    self.insert(node.right,data)
                else:
                    print("L",end="")
                    if node.left == None:
                        node.left = Node(data)
                        print("*",end="")
                        return
                    self.insert(node.left,data)
T = BST()
inp = [int(i) for i in input("Enter Input : ").split()]
for i in inp:
    T.insert(T.root,i)
    print("")