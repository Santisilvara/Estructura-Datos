class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def __insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.__insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.__insert_recursive(node.right, data)

    def __print_preorder(self, node):
        if node:
            print(node.data, end=", ")
            self.__print_preorder(node.left)
            self.__print_preorder(node.right)

    def __print_inorder(self, node):
        if node:
            self.__print_inorder(node.left)
            print(node.data, end=", ")
            self.__print_inorder(node.right)

    def __print_postorder(self, node):
        if node:
            self.__print_postorder(node.left)
            self.__print_postorder(node.right)
            print(node.data, end=", ")

    def insert(self, data):
        if self.root is None: 
            self.root = Node(data)
        else:
            self.__insert_recursive(self.root, data)

    def print_preorder(self):
        self.__print_preorder(self.root)

    def print_inorder(self):
        self.__print_inorder(self.root)

    def print_postorder(self):
        self.__print_postorder(self.root)


tree = BinaryTree()
tree.insert(30)
tree.insert(25)
tree.insert(12)
tree.insert(27)
tree.insert(70)
tree.insert(60)


print("\nPreOrder: ", end="")
tree.print_preorder()
print("\nInOrder: ", end="")
tree.print_inorder()
print("\nPostOrder: ", end="")
tree.print_postorder()