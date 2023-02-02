# Breadth First Search
from collections import deque

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = self.left = None


class BinaryTreeLevelOrderTraversal:
    def __init__(self) -> None:
        self.root = None

    def level_order_traversal(self, root) -> list:
        bfs = []
        if root is None:
            return bfs
        else:
            queue = deque([])
            queue.append(root)
            while len(queue) != 0:
                level_size = len(queue)
                current_level = []
                for i in range(level_size):
                    current_node = queue.popleft()
                    current_level.append(current_node.data)
                    if current_node.left is not None:
                        queue.append(current_node.left)
                    if current_node.right is not None:
                        queue.append(current_node.right)
                bfs.append(current_level)
            return bfs


# Main method
if __name__ == "__main__":
    tree = BinaryTreeLevelOrderTraversal()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    ans = tree.level_order_traversal(tree.root)
    for level in ans:
        print(level)
