from collections import deque


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None


class ZigZagTreeTraversal:
    def __init__(self) -> None:
        self.root = None

    def zigzag_traversal(self, root) -> list[int]:
        zigzag = []
        left_to_right = True
        if root is None:
            return zigzag
        else:
            queue = deque()
            queue.append(root)
            while len(queue) != 0:
                current_level = deque()
                level_size = len(queue)
                for i in range(level_size):
                    current_node = queue.popleft()
                    if left_to_right:
                        current_level.append(current_node.data)
                    else:
                        current_level.appendleft(current_node.data)
                    if current_node.left is not None:
                        queue.append(current_node.left)
                    if current_node.right is not None:
                        queue.append(current_node.right)
                zigzag.append(current_level)
                left_to_right = not left_to_right
            return zigzag


# Main method
if __name__ == "__main__":
    tree = ZigZagTreeTraversal()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    ans = tree.zigzag_traversal(tree.root)
    for level in ans:
        print(level)