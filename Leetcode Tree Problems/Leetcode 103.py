from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        left_to_right = True
        zigzag = []
        if root is None:
            return zigzag
        else:
            queue = deque()
            queue.append(root)
            while len(queue) != 0:
                level_size = len(queue)
                current_level = deque()
                for i in range(level_size):
                    current_node = queue.popleft()
                    if left_to_right:
                        current_level.append(current_node.val)
                    else:
                        current_level.appendleft(current_node.val)
                    if current_node.left is not None:
                        queue.append(current_node.left)
                    if current_node.right is not None:
                        queue.append(current_node.right)
                zigzag.append(current_level)
                left_to_right = not left_to_right
            return zigzag
