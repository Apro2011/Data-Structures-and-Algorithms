# Initializing Node
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = self.left = None


class PathWithGivenSequence:
    def __init__(self) -> None:
        self.root = None

    def find_sequence(self, root, sequence, index) -> bool:
        if root is None:
            return False
        else:
            if index >= len(sequence) or root.data != sequence[index]:
                return False
            elif root.left is None and root.right is None and root.data == sequence[index]:
                return True
            else:
                return self.find_sequence(root.left, sequence, index + 1) or self.find_sequence(root.right, sequence, index + 1)

    def has_path(self, root, sequence) -> bool:
        if root is None:
            return len(sequence) == 0
        return self.find_sequence(root, sequence, 0)


if __name__ == "__main__":
    tree = PathWithGivenSequence()
    tree.root = Node(3)
    tree.root.left = Node(7)
    tree.root.right = Node(1)
    tree.root.left.left = Node(9)
    tree.root.right.left = Node(2)
    tree.root.right.right = Node(5)
    ans = tree.has_path(tree.root, [3, 1, 5])
    print(ans)