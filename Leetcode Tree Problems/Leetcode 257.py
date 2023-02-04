from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def find_path(self, root, string, array):
        if root.left is None and root.right is None:
            array.append(string + str(root.val))
        if root.left is not None:
            self.find_path(root.left, string + str(root.val) + "->", array)
        if root.right is not None:
            self.find_path(root.right, string + str(root.val) + "->", array)

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        else:
            res = []
            self.find_path(root, "", res)
            return res
        