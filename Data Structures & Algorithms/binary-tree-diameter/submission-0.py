# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''

'''
class Solution:
    max_seen = -1
    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Post Order Traversal
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        this_diameter = left + right

        self.max_seen = max(self.max_seen, this_diameter)

        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_seen = -1
        self.dfs(root)
        return self.max_seen





