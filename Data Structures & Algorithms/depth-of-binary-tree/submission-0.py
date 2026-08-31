# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        elif root.left is None and root.right is None: # leaf node reached
            return 1
        
        left = 0 if root.left is None else self.maxDepth(root.left)
        right = 0 if root.right is None else self.maxDepth(root.right)

        return 1 + max(left, right)