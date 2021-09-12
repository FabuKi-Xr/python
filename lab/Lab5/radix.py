class Node:
    def __init__(self,data=None,next=None) -> None:
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0
    def append(self,item):
        newNode = Node(item)
        self.size += 1
        if self.head == None:
            self.head = newNode
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = newNode

    def remove(self,item):
        i = self.head
        before = self.head
        self.size -= 1
        while i != None:
            if item == i.data :
                if i == self.head:
                    self.head = i.next
                    break
                else:
                    before.next = i.next
            before = i
            i = i.next
            
    def __str__(self) -> str:
        i,s =self.head,str(self.head.data)
        while i.next != None:
            s += " -> " + str(i.next.data)
            i = i.next      
        return s

    def max(self):
        i = self.head
        _max = -99999999999999
        while i != None:
            if(i.data > _max):
                _max = i.data
            i = i.next
        return _max

    def round(self):
        round = 0
        val = self.max()
        while val >0:
            val //= 10
            round += 1 
        return round+1 

    def get_digit(self,val,digit):
        for i in range(digit-1):
            val = int(val/10)
        if val >= 0:
            return val % 10
        else:
            return (10-(val%10))%10

    def copy(self):
        i = self.head
        this = LinkedList()
        while i != None:
            this.append(i.data)
            i = i.next
        return this

    def isEmpty(self):
        return self.size == 0
            
    def pop(self):
        self.size -= 1
        i = self.head
        before = self.head
        while i != None:
            if i.next == None:
                before.next = None
                return i.data
            before = i
            i = i.next

    def radixSort(self):
        order = self.copy()
        isStop = False
        q = [LinkedList() for e in range(10)]
        time = 0
        for i in range(1,self.round()+1):
            node = order.head
            print("------------------------------------------------------------")
            print("Round : " + str(i))
            while node != None:
                if self.get_digit(node.data,i) == 0:
                    q[0].append(node.data)
                elif self.get_digit(node.data,i) == 1:
                    q[1].append(node.data)
                elif self.get_digit(node.data,i) == 2:
                    q[2].append(node.data)
                elif self.get_digit(node.data,i) == 3:
                    q[3].append(node.data)
                elif self.get_digit(node.data,i) == 4:
                    q[4].append(node.data)
                elif self.get_digit(node.data,i) == 5:
                    q[5].append(node.data)
                elif self.get_digit(node.data,i) == 6:
                    q[6].append(node.data)
                elif self.get_digit(node.data,i) == 7:
                    q[7].append(node.data)
                elif self.get_digit(node.data,i) == 8:
                    q[8].append(node.data)
                else: q[9].append(node.data)
                node = node.next
            order = LinkedList()
            for j in range(len(q)):
                s = "" 
                if q[0].size == self.size:
                    isStop = True
                while not q[j].isEmpty():
                    temp = q[j].max() 
                    q[j].remove(temp)
                    s += str(temp) + " "
                    order.append(temp)
                print(str(j)+ " : " + s)
            if isStop == True:
                break
            time += 1
        print("------------------------------------------------------------")
        print(str(time)+" Time(s)")
        print("Before Radix Sort : "+str(self))
        print("After  Radix Sort : "+str(order))
    
__input = input("Enter Input : ")
seq = LinkedList()
s = ""
#split
for i in range(len(__input)):
    if __input[i] == ' ':
        seq.append(int(s))
        s = ""
    else:
        s += __input[i]
        if i == len(__input)-1:
            seq.append(int(s))
seq.radixSort()

