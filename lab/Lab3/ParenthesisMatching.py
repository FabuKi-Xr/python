class Stack:
    def __init__(self):
        self.stack = []

    def push(self,i):
        self.stack.append(i) 

    def peek(self):
        return self.stack[-1]

    def pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)
        
    def getstack(self):
        return self.stack

def parenMatch(ex):
    stack = Stack()
    i = 0
    while i< len(ex):
        temp = ex[i]
        if temp in '{[(':
            stack.push(temp)
        else:
            if temp in '}])':
                if(stack.size() > 0):
                    if(not(isMatch(stack.pop(),temp))):
                        return ex + " Unmatch open-close"
                else:
                    return ex + " close paren excess"
        i += 1

    if(stack.size() > 0):
        return ex + " open paren excess   "+ \
               str(stack.size()) +" : "+''.join(map(str,stack.getstack()))
    else:
        return ex + " MATCH"
def isMatch(open,close):
    __open = "([{"
    __close = ")]}"
    return  __open.index(open) == __close.index(close)

myInput = input("Enter expresion : ")
print(parenMatch(myInput))