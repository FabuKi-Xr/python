class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,i):
        self.queue.append(i)
    def size(self):
        return len(self.queue)
    def isEmpty(self):
        return self.size() == 0
    def dequeue(self):
        if(not self.isEmpty()):
            return str((self.queue.pop(0))[1])
        else:
            return "Empty"
    def jump(self,item):
        if self.isEmpty():
            self.enqueue(item)
        else:
            find = False
            for i in range(self.size()):
                if self.queue[i][0] == "EN":  
                    self.queue.insert(i,item)
                    find = True
                    break
            if not find:
                self.enqueue(item)

def PSD48(List):
    q = Queue()
    for i in List:
        temp = i.split()

        if(temp[0] == 'D'):
            print(q.dequeue())

        else:
            if "EN" in temp:
                q.enqueue(temp)
            else:
                q.jump(temp)
                

myInput = input("Enter Input : ").split(",")
PSD48(myInput)
