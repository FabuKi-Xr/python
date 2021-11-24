class Node:
    def __init__(self,key) -> None:
        self.val = key
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self) -> str:
        return str(self.val)

class AVLTree:
    def __init__(self) -> None:
        self.root = None
    def insert(self,key,root=1) :
        if root ==1:
            root = self.root
        if self.root == None:
            self.root = Node(key)
            return
        if not root :
            root = Node(key)
            return root
        elif key < root.val :
            root.left = self.insert(key,root.left)
        else:
            root.right = self.insert(key,root.right)
        root.height = 1+ max(self.getheight(root.left),self.getheight(root.right))
        
        balance  = self.getBalance(root)
        #left left
        if balance > 1 and key < root.left.val :
            print("Not Balance, Rebalance!")
            return self.rRotate(root)
        #right right
        if balance < -1 and key >= root.right.val :
            return self.lRotate(root)
        #left right
        if balance > 1 and key >= root.left.val :
            root.left = self.lRotate(root.left)
            print("Not Balance, Rebalance!")
            return self.rRotate(root)
        #right left
        if balance < -1 and key < root.right.val :
            root.right = self.rRotate(root.right)
            print("Not Balance, Rebalance!")
            return self.lRotate(root)
        return root
    
    def lRotate(self,z) :
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getheight(z.left),self.getheight(z.right))
        y.height = 1 + max(self.getheight(y.left),self.getheight(y.right))
        return y
    
    def rRotate(self,z) :
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1+max(self.getheight(z.left),self.getheight(z.right))
        y.height = 1+max(self.getheight(y.left),self.getheight(y.right))
        return y

    def getheight(self,root) :
        if not root :
            return 0 
        return root.height
    
    def getBalance(self,root) :
        if not root:
            return 0 
        return self.getheight(root.left) - self.getheight(root.right)


    def print_inorder(self,node=1):
        if node == 1:
            node = self.root
        if node != None:
            self.print_inorder(node.left)
            print(node,end=" ")
            self.print_inorder(node.right)
    def print_preorder(self,node=1):
        if node ==1:
            node=self.root
        if node != None:
            print(node,end=" ")
            self.print_preorder(node.left)
            self.print_preorder(node.right)
    def print_postorder(self,node=1):
        if node == 1:
            node = self.root
        if node != None:
            self.print_postorder(node.left)
            self.print_postorder(node.right)
            print(node,end=" ")


print(" *** AVL Tree ***")    

input_string = input("Enter some numbers : ")

bst = AVLTree()

for n in input_string.split():

	bst.insert(int(n))

bst.print_inorder()

bst.print_preorder()

bst.print_postorder()