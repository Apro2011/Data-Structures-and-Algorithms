# Initializing Node
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = self.left = None


# Defining Binary Tree Class
class DepthFirstSearchMaximumPath:
    def __init__(self) -> None:
        self.root = None

    def has_path(self, root, req_sum) -> bool:
        if root is None:
            return False
        elif root.data == req_sum and root.left is None and root.right is None:
            return True
        else:
            return self.has_path(root.left, req_sum-root.data) or self.has_path(root.right, req_sum-root.data)


if __name__ == "__main__":
    tree = DepthFirstSearchMaximumPath()
    tree.root = Node(12)
    tree.root.left = Node(7)
    tree.root.right = Node(1)
    tree.root.left.left = Node(9)
    tree.root.right.left = Node(10)
    tree.root.left.left.left = Node(3)

    print(tree.has_path(tree.root, 23))
