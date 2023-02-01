# Creation of a Binary Tree

# Initializing Node
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = self.left = None


# Defining Binary Tree Class
class BinaryTreeTraversal:
    def __init__(self) -> None:
        self.root = None

    # Pre-Order Traversal
    def pre_order(self, root) -> None:
        if root is None:
            return
        else:
            print(root.data, end=" ")
            self.pre_order(root.left)
            self.pre_order(root.right)

    # In-Order Traversal
    def in_order(self, root) -> None:
        if root is None:
            return
        else:
            self.in_order(root.left)
            print(root.data, end=" ")
            self.in_order(root.right)

    # Post-Order Traversal
    def post_order(self, root) -> None:
        if root is None:
            return
        else:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.data, end=" ")


# Main method
if __name__ == "__main__":
    tree = BinaryTreeTraversal()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    print("Pre-Order Traversal is:", end=" ")
    tree.pre_order(tree.root)
    print()
    print("In-Order Traversal is:", end=" ")
    tree.in_order(tree.root)
    print()
    print("Post-Order Traversal is:", end=" ")
    tree.post_order(tree.root)
    print()
