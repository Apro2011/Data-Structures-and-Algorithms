class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None


class LowestCommonAncestorBinaryTree:
    def __init__(self) -> None:
        self.data = None

    def lowest_common_ancestor(self, root, p, q):
        if root is None:
            return None
        else:
            if root.data == p or root.data == q:
                return root
            left = self.lowest_common_ancestor(root.left, p, q)
            right = self.lowest_common_ancestor(root.right, p, q)
            if left is not None and right is not None:
                return root
            else:
                return left if left is not None else right

    
if __name__ == "__main__":
    tree = LowestCommonAncestorBinaryTree()
    tree.root = Node(3)
    tree.root.left = Node(5)
    tree.root.right = Node(1)
    tree.root.left.left = Node(6)
    tree.root.left.right = Node(2)
    tree.root.right.left = Node(0)
    tree.root.right.right = Node(8)
    tree.root.left.right.left = Node(7)
    tree.root.left.right.right = Node(4)
    ans = tree.lowest_common_ancestor(tree.root, 5, 4)
    print(ans.data)
