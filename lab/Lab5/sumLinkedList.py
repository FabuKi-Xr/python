class Node:
    def __init__(self,data=None,next=None) -> None:
        self.data = data
        self.next = next
class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    def expand(self,ll):
        self.tail.next = ll.head
        return self
    def append(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = newNode
        self.tail = newNode
    def __str__(self):
        i,s = self.head,str(self.head.data)+" "
        while i.next != None:
            s += str(i.next.data)+ " "
            i = i.next
        return s
    def reverse(self):
        before = None
        now = self.head
        while now != None:
            next = now.next
            now.next = before
            before = now
            now = next
        self.head = before
        return self
def split(item):
    L1 = LinkedList()
    L2 = LinkedList()
    temp = L1
    s = ""
    for i in range(0,len(item),1):
        if ' ' == item[i]:
            temp.append(s)
            temp = L2
            s=""
        elif(str(item[i:i+2]) == '->'):
            temp.append(s)
            s=""
        else:
            if item[i] not in '->':
                s += item[i]
            if i == len(item)-1 :
                temp.append(s)

    print("L1    : "+str(L1))      
    print("L2    : "+str(L2))   
    print("Merge : "+str(L1.expand(L2.reverse())))

__input = input("Enter Input (L1,L2) : ")
split(__input)