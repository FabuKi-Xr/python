class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,i):
        self.queue.append(i)
    def dequeue(self):
        self.queue.pop(0)
    def isEmpty(self):
        return len(self.queue) >= 0

class Stack(): #bomb stack
    def __init__(self):
        self.stack = []
        self.item = []
        self.count = 0
    def push(self,i):
        self.stack.append(i)
    def pop(self):
        self.stack.pop()
    def index(self,i):
        return self.getStack().index(i)
    def size(self):
        return len(self.stack)
    def crushBomb(self,q : Queue = None):
        shouldRepeat = True
        while(shouldRepeat):
            for i in range(self.size()):      
                if i+2 < self.size():
                    if self.stack[i] == self.stack[i+1] and \
                        self.stack[i] == self.stack[i+2]:
                        if q == None :
                            self.item.append(self.stack[i])
                            self.pop(i)
                            self.pop(i)
                            self.pop(i)
                        if q != None :
                            if len(q) > 0:
                                if not q.isEmpty() :
                                    self.stack.insert(i+1,q.dequeue()) 
                                    shouldRepeat = True
                                    break
                                else:
                                    self.item.append(self.stack[i])
                                    self.pop(i)
                                    self.pop(i)
                                    self.pop(i)

                        if(self.size()>2):
                            shouldRepeat = False
                        else:
                            shouldRepeat = True
                        break
                    else:
                        shouldRepeat = False
                else:
                    shouldRepeat = False
        return self.item
    
def colorCrush2(normalBomb,mirrorBomb):
    mirrorStack = Stack()
    mirrorq = Queue()
    for i in mirrorBomb[len(mirrorBomb):-1:-1]:
        mirrorStack.push(i)
    for i in mirrorStack.crushBomb():
        mirrorq.enqueue(i)

    # normalStack = Stack() 
    # for i in normalBomb[len(normalBomb):-1:-1]:
    #     normalStack.push(i)
    # normalStack.crushBomb(mirrorq.queue)   
normalBomb,mirrorBomb = input("Enter Input (Normal, Mirror) : ").split()
colorCrush2(normalBomb,mirrorBomb)
