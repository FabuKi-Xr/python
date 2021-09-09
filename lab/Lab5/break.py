class Node:
    def __init__(self,weight=None,fq=None,Next = None) -> None:
        self.front = None
        self.weight = weight
        self.fq = fq
        self.next = Next
class LinkedList():
    def __init__(self) -> None:
        self.head = None
    def add(self,weight,fq): 
        newNode = Node(weight,fq)
        if self.head == None: # null case
            self.head = newNode
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = newNode
    def platebreak(self):
        item = self.head
        pre = Node()
        platebreak = ""
        while item.next != None:
            if item.next.weight > item.weight:
                platebreak += str(item.fq) + "\n"
                pre.next = item.next
                if item == self.head:
                    self.head = item.next  
                item = self.head
            else:
                pre = item
                item = item.next
        return platebreak
    # def __str__(self):
    #     i, s = self.head, str(self.head.weight) + " "
    #     while i.next != None:
    #         s += str(i.next.weight) + " "
    #         i = i.next
    #     return s
L = LinkedList()
__input = input("Enter Input : ").split(',')

for i in __input:

    L.add(int((i.split())[0]),int((i.split())[-1]))
print(L.platebreak(),end="")
