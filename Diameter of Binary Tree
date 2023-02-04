# Initializing Node
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = self.left = None


# Defining Binary Tree Class
class TreeDiameter:
    diameter = 0

    def __init__(self) -> None:
        self.root = None

    def find_height(self, root):
        if not root:
            return 0
        else:
            left_height = self.find_height(root.left)
            right_height = self.find_height(root.right)
            current_diameter = left_height + right_height
            self.diameter = max(self.diameter, current_diameter)
            return max(left_height, right_height) + 1

    def find_diameter(self, root):
        self.find_height(root)
        return self.diameter


# Main method
if __name__ == '__main__':
    tree = TreeDiameter()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.right.left = Node(4)
    tree.root.right.right = Node(5)
    tree.root.right.left.left = Node(6)
    tree.root.right.right.right = Node(7)
    tree.root.right.right.right.left = Node(12)
    tree.root.right.right.right.right = Node(13)
    tree.root.right.left.left.left = Node(8)
    tree.root.right.left.left.right = Node(10)
    tree.root.right.left.left.right.left = Node(11)

    ans = tree.find_diameter(tree.root)
    print(ans)