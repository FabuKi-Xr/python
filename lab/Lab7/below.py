class Node():
    def __init__(self,data=None,left=None,right=None) -> None:
        self.data = data
        self.left = left
        self.right = right
class BST():
    def __init__(self) -> None:
        self.root = None
    def insert(self,data):
        newNode = Node(data)
        if self.root == None:
            self.root = newNode
        else:
            r = self.root
            while True:
                if data < r.data :
                   if r.left == None:
                       r.left = newNode
                       break
                   r = r.left
                else:
                    if r.right == None:
                        r.right = newNode
                        break
                    r = r.right
        return self.root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self.printTree(node.left, level + 1)

def findMin(node:Node,num):
    s = ''
    if node != None:
        s += findMin(node.left, num)
        if num > node.data:
            s+=str(node.data)
        s += " "+findMin(node.right,num)
        return str(s)
    else:
        return ''

T = BST()
inp = input('Enter Input : ').split('|')
for i in inp[0].split():
    root = T.insert(int(i))
T.printTree(T.root)
print("--------------------------------------------------")
output = findMin(root,int(inp[1]))
print(f"Below {inp[1]} : ",end="")
if output.split() == []:
    print("Not have")
print(output)