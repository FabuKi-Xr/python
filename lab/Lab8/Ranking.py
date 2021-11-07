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
    def printTree(self,node,level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def rank(self,node:Node,data,level=0):
        if node == None:
            return level,False
        _level,isFound = self.rank(node.left,data,level)
        if not isFound :
            _level += 1
            if data < node.data:
                return _level,True
            else:
                _level,isFound = self.rank(node.right,data,_level)
        return _level,isFound 

T = BST()
inp = input("Enter Input : ").split('/')
for i in inp[0].split():
    T.insert(T.root,int(i))
T.printTree(T.root)
print('--------------------------------------------------')

rank = T.rank(T.root,int(inp[1]))
rank = rank[0] - 1 if rank[1] else rank[0]
print(f"Rank of {inp[1]} : {(rank)}")