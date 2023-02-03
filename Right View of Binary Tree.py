from collections import deque


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = self.left = None


class BinaryTreeRightView:
    def __init__(self) -> None:
        self.root = None

    def right_view(self, root) -> list[int]:
        result = []
        if root is None:
            return result
        else:
            queue = deque([])
            queue.append(root)
            while len(queue) != 0:
                level_size = len(queue)
                for i in range(level_size):
                    current_node = queue.popleft()
                    if i == level_size - 1:
                        result.append(current_node.data)
                    if current_node.left is not None:
                        queue.append(current_node.left)
                    if current_node.right is not None:
                        queue.append(current_node.right)
            return result


if __name__ == "__main__":
    tree = BinaryTreeRightView()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    tree.root.right.left.left = Node(8)

    ans = tree.right_view(tree.root)
    print(ans)

