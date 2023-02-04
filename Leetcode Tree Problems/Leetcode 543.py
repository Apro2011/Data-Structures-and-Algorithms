from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    diameter = 0

    def find_height(self, root):
        if not root:
            return 0
        else:
            left_height = self.find_height(root.left)
            right_height = self.find_height(root.right)
            current_diameter = left_height + right_height
            self.diameter = max(self.diameter, current_diameter)
            return max(left_height, right_height) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.find_height(root)
        return self.diameter