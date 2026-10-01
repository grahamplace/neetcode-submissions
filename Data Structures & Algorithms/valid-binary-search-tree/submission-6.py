# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root: Optional[TreeNode], rangeMin, rangeMax) -> bool:
        if not root:
            return True
        
        if root.val >= rangeMax or root.val <= rangeMin:
            return False 

        if not self.dfs(root.left, rangeMin, root.val):
            return False
        
        if not self.dfs(root.right, root.val, rangeMax):
            return False
        
        return True
            


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float('-inf'), float('inf'))