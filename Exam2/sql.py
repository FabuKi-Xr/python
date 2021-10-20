from typing import NoReturn


class Node():
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class Linkedlist():
    def __init__(self):
        self.head =None
        self.__size = 0
    
    def append(self,data):
        newNode = Node(data)
        self.__size+=1
        if self.head == None:
            self.head = newNode
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = newNode
    def __str__(self) :
        s = str(self.head.data)
        p = self.head.next
        while p != None :
            s += ' <- '+str(p.data)
            p = p.next
        return s
    def nodeAt(self,i) :
        p = self.head
        for j in range(i) :
            p = p.next
        return p
    def size(self):
        return self.__size
    def reOreder(self):
        t = self.head
        temp = self.head
        prev = Node()
        if self.head.data != 0:
            while t != None:
                if t.data == 0 :
                    self.head = t
                    prev.next = None
                prev = t
                t = t.next
            prev.next = temp
print(" *** Re order ***")
inp = input("Enter Input : ").split()
ll1 = Linkedlist()
ll2 = Linkedlist()
found0 = False
for i in inp:
    ll1.append(int(i))
print("Before :",ll1)
ll1.reOreder()
print("After :",ll1)


