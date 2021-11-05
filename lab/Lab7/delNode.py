# # class Node():
# #     def __init__(self,data) -> None:
# #         self.data = data
# #         self.left = None
# #         self.right = None
# #         self.level = None
# #     def __str__(self) -> str:
# #         return str(self.data)
# # class BinarySearchTree:
# #     def __init__(self) -> None:
# #         self.root = None
    
# #     def insert(self,val):
# #         newNode = Node(val)
# #         print(f"insert {val}")
# #         if self.root == None:
# #             self.root = newNode
# #         else:
# #             node = self.root
# #             while True:
# #                 if node != None:
# #                     if node.data < val:
# #                         if node.right == None:
# #                             node.right = newNode
# #                             return self.root
# #                         else:
# #                             node = node.right
# #                     else:
# #                         if node.left == None:
# #                             node.left = newNode
# #                             return self.root
# #                         else:
# #                             node = node.left
# #         return self.root

# #     def successor(node:Node):
# #         while node.right!= None:
# #             node = node.right
# #         return node

# #     def delete(self,r:Node,data):
# #         isFound = None
# #         if r != None:
# #             if r.data == data:
# #                 print(f"delete {data}")
# #                 if r.left != None and r.right != None:
# #                     successor = self.successor(r)
# #                     r.data = successor
# #                     r.right = self.delete(r.right,successor)
# #                 else:
# #                     if r.left != None:
# #                         return r.left,"Found"
# #                     elif r.right != None:
# #                         return r.right,"Found"
# #                     else:
# #                         return None,"Found"
# #             elif r.data < data:
# #                 r.right,isFound = self.delete(r.right,data)
# #             else:
# #                 r.left,isFound = self.delete(r.left,data)
# #             return isFound
# #         else:
# #             return None,isFound

# # def printTree90(node,level=0):
# #     if node != None:
# #         printTree90(node.right,level+1)
# #         print('     ' * level, node)
# #         printTree90(node.left, level + 1)

# # tree = BinarySearchTree()
# # data = input("Enter Input : ").split(',')
# # for i in data:
# #     if i[0] == 'i':
# #         tree.insert(int(i.split()[-1]))
# #     if i[0] == 'd':
# #         if tree.delete(tree.root,int(i.split()[-1])) == None:
# #             print(f"Error! Not Found DATA")
# #     printTree90(tree.root)
# class Node():
#     def __init__(self,data) -> None:
#         self.data = data
#         self.left = None
#         self.right = None
#         self.level = None
#     def __str__(self) -> str:
#         return str(self.data)
# class BinarySearchTree:
#     def __init__(self) -> None:
#         self.root = None
    
#     def insert(self,val):
#         newNode = Node(val)
#         print(f"insert {val}")
#         if self.root == None:
#             self.root = newNode
#         else:
#             node = self.root
#             while True:
#                 if node != None:
#                     if node.data < val:
#                         if node.right == None:
#                             node.right = newNode
#                             return self.root
#                         else:
#                             node = node.right
#                     else:
#                         if node.left == None:
#                             node.left = newNode
#                             return self.root
#                         else:
#                             node = node.left
#         return self.root

#     def successor(self,node:Node):
#         while node.right!= None:
#             node = node.right
#         return node

#     def delete(self,node:Node,data):
#       if node != None:
#         if node.data < data:
#             self.delete(node.right,data)
#         elif node.data > data:
#             self.delete(node.left,data)
#         else:
#             # if node == self.root:
#             #     if node.right != None:
#             #         temp = self.root.left
#             #         self.root = node.right
#             #         self.root.left = temp
#             #     else:
                    
#             if node.left == node.right == None
#                 return
#             elif node.left and node.right:
#                 successor = self.successor(node.right)
                

# def printTree90(node,level=0):
#     if node != None:
#         printTree90(node.right,level+1)
#         print('     ' * level, node)
#         printTree90(node.left, level + 1)

# tree = BinarySearchTree()
# data = input("Enter Input : ").split(',')
# for i in data:
#     if i[0] == 'i':
#         tree.insert(int(i.split()[-1]))
#     if i[0] == 'd':
#         if tree.delete(tree.root,int(i.split()[-1])) == None:
#             print(f"Error! Not Found DATA")
#     printTree90(tree.root)