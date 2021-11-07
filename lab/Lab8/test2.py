class Node():
    def __init__(self,name,seq,data) -> None:
        self.name = name
        self.data = data
        self.seq = seq
        self.left = None
        self.right = None
    def __str__(self) -> str:
        return str(self.name)
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
            # self.seq.append(self.root)
            return
        if name == node.name*2:
            node.left = Node(name,seq,data)
            # self.seq.append(node.left)
            return
        if name == node.name*2+1:
            node.right = Node(name,seq,data)
            self.seq.append(node.right)
            return
        if node.left != None :
            self.insert(node.left,name,seq,data)
        if node.right != None :
            self.insert(node.right,name,seq,data)
        return self.root

    def reheap(self):
        nodeList = self.seq
        root = self.root
        # while root != None:
        #     if root.left != None and root.right != None:
        #         if root.data > root.left.data:
        #             root.data,root.left.data = root.left.data,root.data
        #             root.name,root.left.name = root.left.name,root.name
        #         elif root.data == root.left
        # for i in range(len(self.seq)):
        #     for j in range(len(self.seq)-1):
        #         if  nodeList[j].data > nodeList[j+1].data:
        #             nodeList[j].name,nodeList[j+1].name = nodeList[j+1].name,nodeList[j].name
        #             nodeList[j].data,nodeList[j+1].data = nodeList[j+1].data,nodeList[j].data
        #         elif nodeList[j].data == nodeList[j+1].data:
        #             if nodeList[j].name > nodeList[j+1].name:
        #                 nodeList[j].name,nodeList[j+1].name = nodeList[j+1].name,nodeList[j].name
        #                 nodeList[j].data,nodeList[j+1].data = nodeList[j+1].data,nodeList[j].data
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('        ' * level, node)
            self.printTree(node.left, level + 1)

    def book(self,data):
        self.root.data += data
        root = self.root
        temp = None
        q = Queue()
        self.printTree(self.root)
        q.enqueue(root.left)
        q.enqueue(root.right)
        heap = []
        while not q.isEmpty():
            node = q.dequeue()
            if node.left != None:
                q.enqueue(node.left)
            if node.right != None:
                q.enqueue(node.right)

            if root.data > node.data:
                node.left = node.right = None
                heap.append(node)
            if root.data < node.data:
                temp = root
                temp.left = temp.right = None
                heap.append(temp)
                temp = None
            if root.data == node.data:
                if root.name < node.name:
                    heap.append(root)
                    heap.append(node)
                else:
                    heap.append(node)
                    heap.append(root)
                temp = None
        if temp != None:
            heap.append(temp)
        self.root = None

        for seq in range(len(heap)):
            self.insert(heap[seq],heap[seq].name,seq+1,heap[seq].data)
        return root.name

inp = input('Enter Input : ').split('/')
bookVan = MinHeap(int(inp[0]))
for cus,day in enumerate(inp[1].split(),1):
    print(f"Customer {cus} Booking Van {bookVan.book(int(day))} | {day} day(s)") 