class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,i):
        self.queue.append(i)
    def dequeue(self):
        return self.queue.pop(0)
    def isEmpty(self):
        return len(self.queue) <= 0

class Stack(): #bomb stack
    def __init__(self,ID):
        self.stack = []
        self.item = []
        self.count = 0
        self.failed = 0
        self.id = ID
    def push(self,i):
        self.stack.append(i)
    def pop(self,i):
        return self.stack.pop(i)
    def size(self):
        return len(self.stack)
    def isEmpty(self):
        return self.size() <= 0
    def bombLeft(self):
        if self.isEmpty():
            if "RORRIM" in self.id:
                return "ytpmE"
            return "Empty"
        self.stack.reverse()
        return ""+''.join(self.stack)

    def crushBomb(self,q : Queue = None):
        shouldRepeat = True
        item = ""
        while(shouldRepeat):
            for i in range(self.size()):      
                if i+2 < self.size():
                    if self.stack[i] == self.stack[i+1] and \
                        self.stack[i] == self.stack[i+2]:

                        if q == None :
                            self.count += 1
                            self.item.append(self.stack[i])
                            self.pop(i)
                            self.pop(i)
                            self.pop(i)

                        if q != None :
                            if not q.isEmpty() :
                                self.stack.insert(i+2,q.dequeue()) 
                                item += self.stack[i+2]
                                shouldRepeat = True
                                if self.stack[i] == self.stack[i+1] and \
                                    self.stack[i] == self.stack[i+2]: #ตัวโดนบวกเพิ่ม
                                    self.failed += 1
                                    self.pop(i)
                                    self.pop(i)
                                    self.pop(i)
                            else:
                                self.count += 1   
                                self.pop(i)
                                self.pop(i)
                                self.pop(i)

                        if(self.size()>2):
                            shouldRepeat = True

                        else:
                            shouldRepeat = False

                        break
                    else:
                        shouldRepeat = False
                else:
                    shouldRepeat = False
        if q == None:
            return self.item
    def result(self):
        if "NORMAL" in self.id:
            print("NORMAL :")
        else:
            print(": RORRIM")
        print(self.size())
        print(self.bombLeft())
        if "NORMAL" in self.id:
            print("{} Explosive(s) ! ! ! (NORMAL)".format(self.count))
        else:
            print("(RORRIM) ! ! ! (s)evisolpxE {}".format(self.count))
        if self.failed > 0:
            print("Failed Interrupted {} Bomb(s)".format(self.failed))
def colorCrush2(normalBomb,mirrorBomb):
    mirrorStack = Stack(": RORRIM")
    mirrorq = Queue()

    for i in range(len(mirrorBomb)-1,-1,-1):
        mirrorStack.push(mirrorBomb[i])
    
    for i in mirrorStack.crushBomb():
        mirrorq.enqueue(i)

    normalStack = Stack(": NORMAL") 
    for i in range(len(normalBomb)):
        normalStack.push(normalBomb[i])
    normalStack.crushBomb(mirrorq)

    normalStack.result()
    print("------------MIRROR------------")
    mirrorStack.result()

normalBomb,mirrorBomb = input("Enter Input (Normal, Mirror) : ").split()
colorCrush2(normalBomb,mirrorBomb)
