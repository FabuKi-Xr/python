class Node:
    def __init__(self,data,Next = None):
        self.data = data
        self.next = Next
class LinkedList:
    def __init__(self):
        self.head = None
        self.__size = 0
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.data) + " "
        while cur.next != None:
            s += str(cur.next.data) + " "
            cur = cur.next
        return s
    def isEmpty(self):
        return self.head == None
    def append(self,item):
        p = Node(item)
        if self.head == None: #null
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
        self.__size += 1
    def addHead(self,item):
        temp = self.head
        self.head = Node(item)
        self.head.next = temp
        self.__size += 1
    def search(self,item):
        i = self.head
        while i != None:
            if item in i.data:
                return "Found "+item
            i = i.next
        return "Not Found "+item
    def index(self,item):
        __index = 0
        i = self.head
        while i != None:
            if item in i.data:
                return __index
            __index += 1
            i = i.next
        return -1
    def size(self):
        return self.__size
    def pop(self,pos):
        i = self.head
        beforeNode = any
        while i != None:
            if self.index(i.data) == pos:
                if i.next != None:
                    beforeNode.next = i.next
                else:
                    self.head = None
                return "Success"
                
            beforeNode = i
            i = i.next
        return "Out of Range"

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{} in {} ".format(L.search(i[3:]),L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)