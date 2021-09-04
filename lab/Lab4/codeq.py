class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,i):
        self.queue.append(i)
        return self.queue

def decode(code):
    q = Queue()
    const = ord(code[0][0])-ord(code[1])
    for i in code[0]:
        print(q.enqueue(chr(ord(i)-const)))
myInput = input("Enter code,hint : ").split(',')
decode(myInput)