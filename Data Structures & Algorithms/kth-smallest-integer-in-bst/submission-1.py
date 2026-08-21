# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Union

class Solution:
    def inorder(self, root: Optional[TreeNode], target: int) -> List[int]:
        if root is None:
            return []
        
        left_result = self.inorder(root.left, target)
        if len(left_result) >= target: return left_result
        
        if len(left_result) + 1 == target: return left_result + [root.val]

        right_res = self.inorder(root.right, target)
        return left_result + [root.val] + right_res
        

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.inorder(root, k)[k - 1]