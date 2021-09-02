class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        return self.stack.pop()

    def push(self,i):
        return self.stack.append(i)

    def getStack(self):
        return self.stack 

def countTree(List):
    bong = False
    stack = Stack()
    for i in List:
        #print(i)
        if(i == 'S'):
            bong = True
        elif i == 'B':
            count = 0
            max = -1
            for j in range(len(stack.getStack())-1,-1,-1):
                if(bong == True):
                    if(stack.getStack()[j]%2 == 1):
                         stack.getStack()[j]= stack.getStack()[j]+2
                    else:
                         stack.getStack()[j] = stack.getStack()[j]-1

                if(max < stack.getStack()[j]):
                    i = 0
                    max = stack.getStack()[j]
                    i += 1    
                    count += 1

            bong = False
            print(count)
        else:
            stack.push(int((i.split())[-1]))
            


myInput = input("Enter Input : ").split(',')
countTree(myInput)
