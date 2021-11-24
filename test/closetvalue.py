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
    def insert(self,node,data):
        if self.root == None:
