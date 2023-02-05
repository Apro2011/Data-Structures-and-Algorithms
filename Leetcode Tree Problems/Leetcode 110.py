from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def height(self, root):
        if not root:
            return 0
        else:
            return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        else:
            left = self.height(root.left)
            right = self.height(root.right)
            if (abs(left - right) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right):
                return True
            else:
                return False