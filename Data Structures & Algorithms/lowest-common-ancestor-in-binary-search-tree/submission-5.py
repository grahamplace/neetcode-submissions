# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val > p.val:
            p_tree = 'left'
        elif root.val == p.val:
            p_tree = 'root'
        else: 
            p_tree = 'right'

        if root.val > q.val:
            q_tree = 'left'
        elif root.val == q.val:
            q_tree = 'root'
        else: 
            q_tree = 'right'
        
        # case 1: p and q are in different subtrees
        if p_tree != q_tree or (p_tree == 'root' and q_tree == 'root'): 
            return root
        elif p_tree == 'root' or q_tree == 'root':
            return root
        elif p_tree == 'right':
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return self.lowestCommonAncestor(root.left, p, q)


