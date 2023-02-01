# Creation of a Binary Tree

# Initializing Node
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = self.left = None


# Defining Binary Tree Class
class BinaryTree:
    def __init__(self) -> None:
        self.root = None


# Main method
if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
