# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_exists = p is not None 
        q_exists = q is not None 
        if not p_exists and not q_exists:
            return True
            
        if (p_exists and not q_exists) or (q_exists and not p_exists):
            return False 

        p_is_leaf = p.left is None and p.right is None
        q_is_leaf = q.left is None and q.right is None
        if p_is_leaf != q_is_leaf:
            return False
        
        if p.val != q.val: return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 
        
