# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSametree(self, a, b) -> bool:
        # Both empty at the same position
        if a is None and b is None:
            return True

        # One is empty but the other is not
        if a is None or b is None:
            return False

        # Values must match, and both children must match exactly
        return (
            a.val == b.val
            and self.isSametree(a.left, b.left)
            and self.isSametree(a.right, b.right)
        )

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root is None or subRoot is None:
            return False

        # Base case: Two leaves are equal if val is equal
        is_a_leaf = root.left is None and root.right is None
        is_b_leaf = subRoot.left is None and subRoot.right is None
        if is_a_leaf and is_b_leaf and root.val == subRoot.val:
            return True

        if root.val == subRoot.val and self.isSametree(root, subRoot): return True

        return (
            self.isSubtree(root.left, subRoot) or 
            self.isSubtree(root.right, subRoot)
        )