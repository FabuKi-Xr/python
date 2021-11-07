class Node():
    def __init__(self,name,seq,data) -> None:
        self.name = name
        self.data = data
        self.seq = seq
        self.left = None
        self.right = None
    def __str__(self) -> str:
        return str(self.name)+" "+str(self.data)
class Queue():

    def __init__(self) -> None:
        self.q = []
    def enqueue(self,node:Node):
        self.q.append(node)
    def dequeue(self):
        return self.q.pop(0)
    def isEmpty(self):
        return len(self.q) == 0 

class MinHeap:
    def __init__(self,n:int) -> None: # n = number of Node
        self.root = None
        self.seq = list()
        for i in range(1,n+1):
            self.insert(self.root,i,i)
    def insert(self,node:Node,name,seq,data=0):
        if self.root == None:
            self.root = Node(name,seq,data)
            return
        if seq == node.seq*2:
            node.left = Node(name,seq,data)
            return
        if seq == node.seq*2+1:
            node.right = Node(name,seq,data)
            return
        if node.left != None :
            self.insert(node.left,name,seq,data)
        if node.right != None :
            self.insert(node.right,name,seq,data)
        return self.root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('        ' * level, node)
            self.printTree(node.left, level + 1)

    def book(self,data):
        self.root.data += data
        name = self.root.name
        temp = self.root
        
        q = Queue()

        if temp.left != None:
            q.enqueue(temp.left)
        if temp.right != None:
            q.enqueue(temp.right)
        heap = []

        while not q.isEmpty():
            node = q.dequeue()
            if node.left != None:
                q.enqueue(node.left)
            if node.right != None:
                q.enqueue(node.right)
    
            if temp and temp.data < node.data:
                temp.left = temp.right = None
                heap.append(temp)
                temp = None
            if temp and temp.data == node.data:
                if temp.name < node.name:
                    temp.left = temp.right = None
                    heap.append(temp)
                    temp = None

            node.left = node.right = None
            heap.append(node)

        if temp != None:
            heap.append(temp)
        self.root = None

        for seq in range(len(heap)):
            self.insert(self.root,heap[seq].name,seq+1,heap[seq].data)
        return name

inp = input('Enter Input : ').split('/')
bookVan = MinHeap(int(inp[0]))
for cus,day in enumerate(inp[1].split(),1):
    print(f"Customer {cus} Booking Van {bookVan.book(int(day))} | {day} day(s)") 