from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_sum = float("-inf")

    def find_sum(self, root):
        if not root:
            return 0
        else:
            left_sum = self.find_sum(root.left)
            right_sum = self.find_sum(root.right)
            left_sum = max(left_sum, 0)
            right_sum = max(right_sum, 0)
            current_sum = left_sum + right_sum + root.val
            self.max_sum = max(current_sum, self.max_sum)
            return max(left_sum, right_sum) + root.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.find_sum(root)
        return self.max_sum