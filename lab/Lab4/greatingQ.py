class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,i):
        self.queue.append(i)
    def dequeue(self): 
        return self.queue.pop(0)
        
    def isEmpty(self):
        return len(self.queue) == 0

myInput = input("Enter Input : ").split(',')
q = Queue()
deqList = []
for i in myInput:
    if(i == 'D'):
        if(q.isEmpty()):
            print("Empty")
        else:
            deqList.append(q.dequeue())
            print(str(deqList[-1])+" <- ",end="")
            if(q.isEmpty()):
                 print("Empty")
            else:
                print(*q.queue,sep=', ')
        
    else:
        q.enqueue(int((i.split())[-1]))
        print(*q.queue,sep=', ')
if(len(deqList) == 0):
    print("Empty",end="")
print(*deqList,sep=', ',end="")
print(" : ",end="")
print(*q.queue,sep=', ',end="")
if(q.isEmpty()):
    print("Empty")



