# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Union

class Solution:
    def inorder(self, root: Optional[TreeNode], arr: List[int], target: int) -> List[int]:
        if root is None:
            return []
        
        left_result = self.inorder(root.left, arr, target)
        right_res = self.inorder(root.right, arr, target)

        return left_result + [root.val] + right_res
        

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.inorder(root, [], k)[k - 1]