# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()    

        if root is None:
            return []

        q.append(root)
        output = []
        while len(q) > 0:
            level_vals = []

            for _ in range(len(q)):
                curr = q.popleft()
                # process popped
                level_vals.append(curr.val)

                # enqueue popped left and right
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)

            output.append(level_vals)
        
        return output
