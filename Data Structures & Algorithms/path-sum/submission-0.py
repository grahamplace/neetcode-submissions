# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _has_path_sum(self, root: Optional[TreeNode], targetSum: int, sumStack: List[int]) -> bool:
        if root is None:
            return False

        # base case: we reach a leaf node:
        if not root.left and not root.right:
            return targetSum == sumStack[-1] + root.val
        
        sumStack.append(sumStack[-1] + root.val)

        # otherwise, check left and right
        if root.left and self._has_path_sum(root.left, targetSum, sumStack):
            return True

        if root.right and self._has_path_sum(root.right, targetSum, sumStack):
            return True
        
        # if reached, there are children but this node has no viable path, so we should pop from stack 
        sumStack.pop()
        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sum_stack = [0]
        return self._has_path_sum(root, targetSum, sum_stack)