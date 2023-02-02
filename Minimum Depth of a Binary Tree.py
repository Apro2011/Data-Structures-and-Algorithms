from collections import deque

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = self.left = None


class BinaryTreeMinimumDepth:
    def __init__(self) -> None:
        self.root = None

    def find_minimum_depth(self, root) -> int:
        minimum_depth = 0
        if root is None:
            return minimum_depth
        else:
            queue = deque([])
            queue.append(root)
            while len(queue) != 0:
                minimum_depth += 1
                level_size = len(queue)
                for i in range(level_size):
                    current_node = queue.popleft()
                    if current_node.left is None and current_node.right is None:
                        return minimum_depth
                    if current_node.left is not None:
                        queue.append(current_node.left)
                    if current_node.right is not None:
                        queue.append(current_node.right)
            return minimum_depth



if __name__ == "__main__":
    tree = BinaryTreeMinimumDepth()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    ans = tree.find_minimum_depth(tree.root)
    print(ans)