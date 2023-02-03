class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = self.left = None


class SumRootToLeafPaths:
    def __init__(self) -> None:
        self.root = None

    def find_path_sum(self, root, path_sum):
        if root is None:
            return 0
        else:
            path_sum = 10 * path_sum + root.data
            if root.left is None and root.right is None:
                return path_sum
            else:
                return self.find_path_sum(root.left, path_sum) + self.find_path_sum(root.right, path_sum)

    def find_sum_path_numbers(self, root):
        return self.find_path_sum(root, 0)


if __name__ == "__main__":
    tree = SumRootToLeafPaths()
    tree.root = Node(3)
    tree.root.left = Node(7)
    tree.root.right = Node(1)
    tree.root.left.left = Node(9)
    tree.root.right.left = Node(4)
    tree.root.right.right = Node(5)

    ans = tree.find_sum_path_numbers(tree.root)
    print(ans)