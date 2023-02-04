class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = self.right = None

class MaxPathSum:
    max_sum = float("-inf")
    
    def __init__(self) -> None:
        self.data = None

    def find_max_sum_recursive(self, root):
        if not root:
            return 0
        else:
            left_sum = self.find_max_sum_recursive(root.left)
            right_sum = self.find_max_sum_recursive(root.right)
            left_sum = max(left_sum, 0)
            right_sum = max(right_sum, 0)
            current_sum = left_sum + right_sum + root.data
            self.max_sum = max(self.max_sum, current_sum)
            return max(left_sum, right_sum) + root.data

    def find_max_sum(self, root):
        self.find_max_sum_recursive(root)
        return self.max_sum


if __name__ == '__main__':
    tree = MaxPathSum()
    tree.root = Node(10)
    tree.root.left = Node(2)
    tree.root.right = Node(10)
    tree.root.left.left = Node(20)
    tree.root.left.right = Node(1)
    tree.root.right.left = Node(-25)
    tree.root.right.left.left = Node(3)
    tree.root.right.left.right = Node(4)
    ans = tree.find_max_sum(tree.root)
    print(ans)
