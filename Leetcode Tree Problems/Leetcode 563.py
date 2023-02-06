from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    tilt = 0
    def working(self, root):
        if not root:
            return 0
        else:
            left = self.working(root.left)
            right = self.working(root.right)
            self.tilt += abs(left-right)
            return left + right + root.val

    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.working(root)
        return self.tilt