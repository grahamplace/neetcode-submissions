# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def compare(self, a, b) -> bool:
        return abs(a - b) <= 1

    def check_node(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            left_h = self.check_node(root.left)
            if left_h == -1: return -1 
            right_h = self.check_node(root.right)
            if right_h == -1: return -1 
            is_balanced = self.compare(left_h, right_h)
            return -1 if not is_balanced else 1 + max(left_h, right_h)
   

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        # inorder traversal of every node - left, root, right
        left_res = self.check_node(root.left)
        if left_res == -1:
            return False

        right_res = self.check_node(root.right)
        if right_res == -1:
            return False
        
        return self.compare(left_res, right_res)
        
