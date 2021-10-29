class Node():
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)
class Queue():
    def __init__(self) -> None:
        self.queue = []
    def dequeue(self):
        if len(self.queue)==0:
            return None
        return self.queue.pop(0)
    def enqueue(self,node:Node):
        self.queue.append(node)

class BST():
    def __init__(self) -> None:
        self.root = None
        self.q = Queue()
    def insert(self,node:Node,data):
        if self.root == None:
            self.root = Node(data)
            return
        if node != None:
            if data < node.data:
                if node.left == None:
                    node.left = Node(data)
                    return
                self.insert(node.left,data)
            else:
                if node.right == None:
                    node.right = Node(data)
                    return
                self.insert(node.right,data)

        else: 
            return
    def printIn(self,node:Node):
        if node != None:
            self.printIn(node.left)
            print(node,end=" ")
            self.printIn(node.right)
    def printPre(self,node:Node):
        if node != None:
            print(node,end=" ")
            self.printPre(node.left)
            self.printPre(node.right)
    def printPost(self,node:Node):
        if node != None:
            self.printPost(node.left)
            self.printPost(node.right)
            print(node,end=" ")
    def printBreath(self,node:Node):
        if node != None:
            if node.left != None:
                self.q.enqueue(node.left)
            if node.right != None:
                self.q.enqueue(node.right)
            print(node,end=" ")
            self.printBreath(self.q.dequeue())

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    T.insert(T.root,i)
print("Preorder : ",end="")
T.printPre(T.root)
print("\nInorder : ",end="")
T.printIn(T.root)
print("\nPostorder : ",end="")
T.printPost(T.root)
print("\nBreadth : ",end="")
T.printBreath(T.root)

    
        