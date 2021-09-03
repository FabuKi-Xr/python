class Stack:

    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self,i):
        return self.stack.pop(i)
    def size(self):
        return len(self.stack)
    def isEmpty(self):
        return len(self.stack) == 0
    def index(self,i):
        return self.getStack().index(i)
    def getStack(self):
        return self.stack
    def reverse(self):
        return self.stack.reverse()
        
def Game(List):
    shouldRepeat = True
    combo = 0
    while(shouldRepeat):
        for i in stack.getStack():
            if(stack.index(i)+2<len(stack.getStack())):#
                if(i == stack.getStack()[stack.index(i)+1] \
                and i == stack.getStack()[stack.index(i)+2] ):#
                    
                    combo += 1
                    stack.pop(stack.index(i))#
                    stack.pop(stack.index(i))#
                    stack.pop(stack.index(i))#

                    if(stack.size() > 2):
                        shouldRepeat = True
                        break;
                    else :
                        shouldRepeat = False
                        break;
                else:
                    shouldRepeat = False
            else:
                shouldRepeat = False
    
    result(stack,combo)

def result(stack,combo):
    print(stack.size())
    stack.reverse() #
    if not stack.isEmpty():
         print(''.join(map(str,stack.getStack())))
    if(stack.isEmpty()):
        print("Empty")
    if(combo > 1):
        print("Combo : {} ! ! !".format(combo))

inp = input('Enter Input : ').split()
stack = Stack()
for i in inp:
    stack.push(i)
Game(stack)

