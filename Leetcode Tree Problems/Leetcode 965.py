from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterative - Breadth First Search
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return None
        else:
            queue = deque([])
            queue.append(root)
            while queue:
                level_size = len(queue)
                for i in range(level_size):
                    current_node = queue.popleft()
                    if current_node.left:
                        if current_node.left.val != current_node.val:
                            return False
                        else:
                            queue.append(current_node.left)
                    if current_node.right:
                        if current_node.right.val != current_node.val:
                            return False
                        else:
                            queue.append(current_node.right)
            return True


# Recursive - Depth First Search

class Solution:
    def working(self, root, check):
        if not root:
            return True
        else:
            if root.val == check:
                return self.working(root.left, check) and self.working(root.right, check)
            elif root.val != check:
                return False

    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        check = root.val
        return self.working(root, check)