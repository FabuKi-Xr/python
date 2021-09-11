class Node:
    def __init__(self,data=None,next=None) -> None:
        self.data = data
        self.next = next
class Linkedlist:
    def __init__(self) -> None:
        self.head = None
        self.tail = Node('|')
    def append(self,item):
        newNode = Node(item,self.tail)
        if self.head == None:
            self.head = newNode
        else:
            t = self.head
            while t.next != self.tail:
                if t.next.data == '|':
                    newNode.next = t.next
                    break
                t = t.next
            t.next = newNode
    def __str__(self):
        i,s = self.head,str(self.head.data)+" "
        while i.next != None:
            s+= i.next.data+ " "
            i = i.next
        return s
    def cursorLeft(self):
        if(self.head != None):
            i = self.head
            while i.next != None:
                if i.next.data == '|':
                    temp = i.next.data
                    i.next.data = i.data
                    i.data = temp
                    #break
                i = i.next
    def cursorRight(self):
        if self.head != None:
            i = self.head
            while i.next != None:
                if i.data == '|':
                    i.data,i.next.data = i.next.data,i.data
                    break
                i = i.next
    def deleteLeft(self):
        i = self.head
        before = self.head
        while i.next != None:
            if i.next.data == '|':
                before.next = i.next       
            before = i
            i = i.next
    def deleteRight(self):
        i = self.head
        before = self.head
        while i.next != None:
            if i.data == '|':
                i.next = i.next.next
                break
            i = i.next
def VIM(input):
    L = Linkedlist()
    s = ""

    for i in range(len(input)):
        
        if input[i] ==',' or i==len(input)-1:
            if i==len(input)-1:
                s += input[i]
            if(s[0]=='I'):
                L.append(s[2:])  
            elif(s[0] == 'L'):
                L.cursorLeft()
            elif s[0] == 'R':
                L.cursorRight()
            elif s[0] == 'B':
                L.deleteLeft()
            elif s[0] == 'D':
                L.deleteRight()
            s=""
        else: 
            s +=input[i]
    print(L)      
__input = input("Enter Input : ")
VIM(__input)
