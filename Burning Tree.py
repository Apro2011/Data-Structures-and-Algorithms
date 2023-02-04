from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None

class BurningTree:
    
    def __init__(self): 
        self.root = None

    queue = deque([])

    def burning_tree(self, root, target_node):
        if root is None:
            return 0
        if root.data == target_node:
            print(root.data)
            if root.left:
                self.queue.append(root.left)
            if root.right:
                self.queue.append(root.right)
            return 1

        left = self.burning_tree(root.left, target_node)
        if left == 1:
            queuesize = len(self.queue)
            for i in range(queuesize):
                current = self.queue.popleft()
                print(current.data, end=" ")
                if current.left:
                    self.queue.append(current.left)
                if current.right:
                    self.queue.append(current.right)
            if root.right:
                self.queue.append(root.right)
            print(root.data)
            return 1

        right = self.burning_tree(root.right, target_node)
        if right == 1:
            queuesize = len(self.queue)
            for i in range(queuesize):
                current = self.queue.popleft()
                print(current.data, end=" ")
                if current.left:
                    self.queue.append(current.left)
                if current.right:
                    self.queue.append(current.right)
            if root.left:
                self.queue.append(root.left)
            print(root.data)
            return 1
        return 0

    def print_burning_tree(self, root, target_node):
        self.burning_tree(root, target_node)
        while self.queue:
            queuesize = len(self.queue)
            for i in range(queuesize):
                current = self.queue.popleft()
                print(current.data, end=" ")
                if current.left is not None:
                    self.queue.append(current.left)
                if current.right is not None:
                    self.queue.append(current.right)
            print()


if __name__ == '__main__':
    tree = BurningTree()
    tree.root = Node(3)
    tree.root.left = Node(5)
    tree.root.right = Node(1)
    tree.root.left.left = Node(6)
    tree.root.left.right = Node(2)
    tree.root.right.left = Node(0)
    tree.root.right.right = Node(8)
    tree.root.left.right.left = Node(7)
    tree.root.left.right.right = Node(4)
    tree.print_burning_tree(tree.root, 2)