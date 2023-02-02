from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        minimum_depth = 0
        if not root:
            return minimum_depth
        else:
            queue = deque([])
            queue.append(root)
            while len(queue):
                minimum_depth += 1
                level_size = len(queue)
                for i in range(level_size):
                    current_node = queue.popleft()
                    if not current_node.left and not current_node.right:
                        return minimum_depth
                    if current_node.left:
                        queue.append(current_node.left)
                    if current_node.right:
                        queue.append(current_node.right)
            return minimum_depth