class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
    def push(self,i):
        self.stack.append(i) 
        self.size += 1
        return "Add = {} and Size = {}".format(i,self.size)
    def popout(self):
        self.tempStack = self.stack.copy()
        if(self.size > 0):
            self.temp = self.stack.pop()
            self.size -=1 
            return "Pop = {} and Index = {}".format(self.temp,self.tempStack.index(self.temp))
        else:
            return "-1"
    def getStack(self):
        if(self.size>0):
            return "Value in Stack = "+' '.join(map(str,self.stack))
        else:
            return "Value in Stack = Empty"
def mode(pureList):
    stack = Stack()
    for i in pureList:
        if(i[0] == 'A'):
            print(stack.push(int((i.split())[1])))
        if(i[0] == 'P'):
            print(stack.popout())
    print(stack.getStack())
myInput = [e for e in input("Enter Input : ").split(',')]
mode(myInput)