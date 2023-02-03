from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_level = 1
        level = 0
        if not root:
            return None
        else:
            max_sum = root.val
            queue = deque([])
            queue.append(root)
            while queue:
                level_size = len(queue)
                current_level = []
                for i in range(level_size):
                    current_node = queue.popleft()
                    current_level.append(current_node.val)
                    if current_node.left:
                        queue.append(current_node.left)
                    if current_node.right:
                        queue.append(current_node.right)
                current_level_sum = sum(current_level)
                level += 1
                if current_level_sum > max_sum:
                    max_sum = current_level_sum
                    max_level = level
            return max_level
                