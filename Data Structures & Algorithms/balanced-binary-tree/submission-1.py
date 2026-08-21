# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def computeHeight(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        else:
            return 1 + max(self.computeHeight(root.left), self.computeHeight(root.right))


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        # inorder traversal of every node - left, root, right
        if root.left and not self.isBalanced(root.left):
            return False

        if root.right and not self.isBalanced(root.right):
            return False
        
        return abs(self.computeHeight(root.left) - self.computeHeight(root.right)) <= 1
        
