class Stack():
    def __init__(self) -> None:
        self.s = []
        self.__size = 0
    def push(self,data):
        self.s.append(data)
        self.__size += 1
    def pop(self):
        self.__size -= 1
        return self.s.pop()
    def isEmpty(self):
        return self.__size == 0
    def size(self):
        return self.__size
    def peek(self):
        if not self.isEmpty():
            return self.s[-1]
        else:
            return -1
    def bottom(self):
        if not self.isEmpty():
            return self.s[0]
        return -1
    def __str__(self) -> str:
        return "Data in Stack is : "+' '.join(map(str,self.s))
inp = input("Enter choice : ")
if inp == '1' :
    s1 = Stack()
    s1.push(10)
    s1.push(20)
    print(s1)
    s1.pop()
    s1.push(30)
    print("Peek of stack :",s1.peek())
    print("Bottom of stack :",s1.bottom())
if inp == '2':
    s1 = Stack()
    s1.push(100)
    s1.push(200)
    s1.push(300)
    s1.pop()
    print(s1)
    print("Stack is Empty :",s1.isEmpty())
if inp == '3':
    s1 = Stack()
    s1.push(11)
    s1.push(22)
    s1.push(33)
    s1.pop()
    print(s1)
    print("Stack size :",s1.size())
     