from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        bfs = deque()
        if not root:
            return bfs
        else:
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
                bfs.appendleft(current_level)
            return bfs
