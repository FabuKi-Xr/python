class Node:
    def __init__(self,data,left=None,right=None) -> None:
        self.data = data
        self.left = left
        self.right = right
    def __str__(self) -> str:
        return str(self.data)

class BST():
    def __init__(self) -> None:
        self.root = None
        