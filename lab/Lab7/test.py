class Node():
    def __init__(self,data=None) -> None:
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)
class Stack():
    def __init__(self) -> None:
        self.stack = []
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        return self.stack.pop()
class BST():
    def __init__(self) -> None:
        self.root = None
        self.stack = Stack()

    def insert(self,node:Node,data):
        if self.root == None:
            self.root = Node(data)
            return
        if node != None:
            if node.data in '+-*/':    
                if node.right == None :
                    node.right = Node(data)
                    return
                self.insert(node.right,data)
            else:
                return
            if node.left == None:
                node.left = Node(data)
                return
            self.insert(node.left,data) 

        else: 
            return
    def printTree(self,node:Node,level=0):
        self.printTree(node.right, level + 1)
        print('     ' * level, node)
        self.printTree(node.left, level + 1)
T = BST()
inp = input("Enter Postfix : ")
for i in inp[::-1]:
    T.insert(T.root,i)
print("Tree : ")
T.printTree(T.root)
'''
    class Node():
    def __init__(self,data=None) -> None:
        self.data = data
        self.left = None
        self.right = None
    # def canAdd(self):
    #     return (self.right == '+-*/') == (self.left == '+-*/')
    def __str__(self):
        return str(self.data)
class Stack():
    def __init__(self) -> None:
        self.stack = []
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        return self.stack.pop()
class BST():
    def __init__(self) -> None:
        self.root = None
        #self.stack = Stack()

    def insert(self,node:Node,data):
        if self.root == None:
            self.root = Node(data)
            return
        if node != None:
            if node.right != None:
                if node.right.data not in '+-*/':
                    if node.left != None:
                        if node.left.data not in '+-*/':
                            return
                        self.insert(node.right,data)
                            
                    else:
                        node.left = Node(data)
                else:
                    self.insert(node.right,data)
            else:
                node.right = Node(data)
            #return True
    def printTree(self,node:Node,level=0):
        self.printTree(node.right, level + 1)
        print('     ' * level, node)
        self.printTree(node.left, level + 1)
        
T = BST()
inp = input("Enter Postfix : ")
for i in inp[::-1]:
    T.insert(T.root,i)
# print("Tree : ")
# T.printTree(T.root)
'''