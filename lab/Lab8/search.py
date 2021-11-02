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
        self.max = -999999999999999
        self.min = 999999999999999
    def insert(self,node:Node,data):
        if self.root == None:
            self.root = Node(data)
        else:
            if node != None:
                if node.data < data:
                    if node.right == None:
                        if self.max < data:
                            self.max = data
                        node.right = Node(data)
                        return
                    self.insert(node.right,data)
                else:
                    if node.left == None:
                        if self.min > data:
                            self.min = data
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
                isFound = closestValue(root.right,value)
                if isFound != "Found":
                    if value in range(root.data,root.right.data+1):
                        if abs(value-root.data) <= abs(value-root.right.data) and root.data >=0:
                            print(f"Closest value of {value} : {root.data}")
                        else:
                            print(f"Closest value of {value} : {root.right.data}")
                        isFound = "Found"
                return isFound
        else:
            if root.left != None:
                isFound = closestValue(root.left,value)
                if isFound != "Found":
                    if value in range(root.left.data,root.data+1):
                        if abs(value-root.data) <= abs(value-root.left.data):
                            print(f"Closest value of {value} : {root.data}")
                        else:
                            print(f"Closest value of {value} : {root.left.data}")
                        isFound = "Found"
                return isFound

T = BST()
inp = input("Enter Input : ").split('/')
for i in inp[0].split():
    T.insert(T.root,int(i))
    T.printTree(T.root)
    print("--------------------------------------------------")
find = int(inp[1])
if closestValue(T.root,find) == None:
    if abs(T.max - find) <= abs(T.min - find):
        print(f"Closest value of {find} : {T.max}")
    else:
        print(f"Closest value of {find} : {T.min}")
