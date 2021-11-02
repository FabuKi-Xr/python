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
            self.root = Node(data)
        else:
            if node != None:
                if node.data < data:
                    if node.right == None:
                        node.right = Node(data)
                        return
                    self.insert(node.right,data)
                else:
                    if node.left == None:
                        node.left = Node(data)
                        return
                    self.insert(node.left,data)

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
def closestValue(root:Node,value)  -> int:
    if root != None:
        if root.data <= value :
            if root.right != None:
                if value in range(root.data,root.right.data+1):
                    if abs(value-root.data) <= abs(value-root.right.data):
                        print(f"Closest value of {value} : {root.data}")
                        return
                    print(f"Closest value of {value} : {root.right.data}")
            closestValue(root.right,value)
        else:
            if root.left != None:
                if value in range(root.left.data,root.data+1):
                    if abs(value-root.data) <= abs(value-root.left.data):
                        print(f"Closest value of {value} : {root.data}")
                        return
                    print(f"Closest value of {value} : {root.left.data}")
            closestValue(root.left,value)

T = BST()
inp = input("Enter Input : ").split('/')
for i in inp[0].split():
    T.insert(T.root,int(i))
    # T.printTree(T.root)
    # print("--------------------------------------------------")
closestValue(T.root,int(inp[1]))
