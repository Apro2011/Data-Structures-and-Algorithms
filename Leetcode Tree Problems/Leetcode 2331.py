from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 0
        else:
            root.left = self.evaluateTree(root.left)
            root.right = self.evaluateTree(root.right)
            if root.val == 2:
                return root.left or root.right
            elif root.val == 3:
                return root.left and root.right
            elif root.val == 0:
                return False
            else:
                return True