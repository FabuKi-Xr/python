class Node():
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
    def __str__(self) -> str:
        return str(self.data)

class BST():
    def __init__(self) -> None:
        self.root = None
    def insert(self,itemlist:list):

        for i in range(len(itemlist)):
            if i*2 < len(itemlist)-1:
                itemlist[i].left = itemlist[i*2+1]
            else:
                break
            if i*2+1 < len(itemlist)-1:
                itemlist[i].right = itemlist[i*2+2]
            if self.root == None:
                self.root = itemlist[i]
        return self.root

    def atk(self,root:Node):
        if root == None:
            return 0
        _atk = self.atk(root.left)
        return root.data + self.atk(root.right) + _atk

T = BST()
inp = input('Enter Input : ').split('/')
itemlist = [Node(int(e)) for e in inp[0].split()] 
root = T.insert(itemlist)
print(T.atk(T.root))

for i in inp[1].split(','):
    comp = i.split()
    if T.atk(itemlist[int(comp[0])]) > T.atk(itemlist[int(comp[1])]):
        print(f"{int(comp[0])}>{int(comp[1])}")
    elif T.atk(itemlist[int(comp[0])]) == T.atk(itemlist[int(comp[1])]):
        print(f"{int(comp[0])}={int(comp[1])}")
    else:
        print(f"{int(comp[0])}<{int(comp[1])}")
