from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    final_sum = 0

    def working(self, root):
        if not root:
            return None
        else:
            if not (root.val % 2):
                if root.left:
                    if root.left.left:
                        self.final_sum += root.left.left.val
                    if root.left.right:
                        self.final_sum += root.left.right.val
                    
                    
                if root.right:
                    if root.right.left:
                        self.final_sum += root.right.left.val
                    if root.right.right:
                        self.final_sum += root.right.right.val
            self.working(root.left)
            self.working(root.right)
    

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.working(root)
        return self.final_sum

