class Queue():
    def __init__(self) -> None:
        self.q = []
    def enqueue(self,data):
        self.q.append(data)
    def dequeue(self):
        self.q.pop(0)
    def isDuplicate(self) -> str:
        for i in self.q:
            count = 0
            for j in self.q:
                if i == j:
                    count +=1
                if count >1:
                    return "Duplicate"
        return "NO Duplicate"
    def __str__(self):
        return str(self.q)
inp = input("Enter Input : ").split('/')
q = Queue()
for i in inp[0].split():
    q.enqueue(int(i))

for i in inp[1].split(','):
    if i[0] == 'E':
        q.enqueue(int((i.split())[-1]))
    if i[0] == 'D':
        q.dequeue()
print(q.isDuplicate())
