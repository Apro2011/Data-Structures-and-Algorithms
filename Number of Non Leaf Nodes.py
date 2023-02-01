class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None


class NumberOfNonLeafNodesInBinaryTree:
    def __init__(self) -> None:
        self.root = None

    def pre_order(self, root) -> None:
        if root is None:
            return
        else:
            print(root.data, end=" ")
            self.pre_order(root.left)
            self.pre_order(root.right)

    def count_non_leaf_nodes(self, root) -> int:
        if root is None:
            return
        elif root.left != None or root.right != None:
            return 1 + self.count_non_leaf_nodes(root.left) + self.count_non_leaf_nodes(root.right)
        else:
            return 0


if __name__ == "__main__":
    tree = NumberOfNonLeafNodesInBinaryTree()
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
    print(tree.count_non_leaf_nodes(tree.root))