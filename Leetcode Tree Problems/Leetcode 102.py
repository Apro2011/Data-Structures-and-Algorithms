from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        bfs = []
        if root is None:
            return bfs
        else:
            queue = deque([])
            queue.append(root)
            while len(queue) != 0:
                current_level = []
                level_size = len(queue)
                for i in range(level_size):
                    current_node = queue.popleft()
                    current_level.append(current_node.val)
                    if current_node.left is not None:
                        queue.append(current_node.left)
                    if current_node.right is not None:
                        queue.append(current_node.right)
                bfs.append(current_level)
            return bfs