from collections import deque


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None


class LevelOrderSuccessor:
    def __init__(self) -> None:
        self.root = None

    def find_successor(self, root, key) -> int:
        if root is None:
            return None
        else:
            queue = deque([])
            queue.append(root)
            while len(queue) != 0:
                current_node = queue.popleft()
                if current_node.left is not None:
                    queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)
                if current_node.data == key:
                    break
            return queue.popleft()


if __name__ == "__main__":
    tree = LevelOrderSuccessor()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    ans = tree.find_successor(tree.root, 6)
    print(ans.data)
