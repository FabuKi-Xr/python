class Node:
    def __init__(self,data,left=None,right=None) -> None:
        self.data = data
        self.left = left
        self.right = right
    def __str__(self) -> str:
        return str(self.data)

class BST():
    def __init__(self) -> None:
        self.root = None
    def insert(self,node:Node,data):
        if self.root == None:
            self.root = Node(data)
            print("*")
            return
        
        if node == None:
            return

        if node.data < data:
            print("R",end="")
            if node.right == None:
                node.right = Node(data)
                print("*")
            else:
                self.insert(node.right,data)
        else:
            print("L",end="")
            if node.left == None:
                node.left = Node(data)
                print("*")
            else:
                self.insert(node.left,data)
        
inp = input('Enter Input : ').split()
tree = BST()
for i in inp:
    tree.insert(tree.root,int(i))


            
