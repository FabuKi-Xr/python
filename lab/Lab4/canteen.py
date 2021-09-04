class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,item):
        if self.isEmpty():
            self.queue.append(item)
        else:
            find = False
            for i in range(self.size()-1,-1,-1):
                if(item[0] == (self.queue)[i][0]):
                    self.queue.insert(i+1,item)
                    find = True
                    break
            if not find:
                self.queue.append(item)  
    def size(self):
        return len(self.queue)
    def isEmpty(self):
        return self.size() == 0
    def dequeue(self):
        if self.isEmpty():
            return "Empty"
        return str((self.queue.pop(0))[-1]) 

def canteen(List):
    q = Queue()
    for i in range(len(List[-1])):
        seq = List[-1][i] # sequence after / 
        if seq == 'D':
            pass
            print(q.dequeue())
        else:   #E
            for j in range(len(List[0])):
                if (seq.split())[-1] in List[0][j]:
                    q.enqueue([((List[0][j]).split())[0],(seq.split())[-1]]) # department,id
myInput = [e.split(',') for e in input("Enter Input : ").split('/')]
canteen(myInput)
