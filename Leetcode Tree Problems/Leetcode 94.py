from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def working(self, root, final_list):
        if not root:
            return None
        else:
            self.working(root.left, final_list)
            final_list.append(root.val)
            self.working(root.right, final_list)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        final_list = []
        self.working(root, final_list)
        return final_list
            