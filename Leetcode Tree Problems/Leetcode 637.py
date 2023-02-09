from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return None
        else:
            ans = []
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
                average = round((sum(current_level) / level_size), 5)
                ans.append(average)
            return ans
