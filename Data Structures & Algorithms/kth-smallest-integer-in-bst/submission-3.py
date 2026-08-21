# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            # go all the way left:
            while curr:
                stack.append(curr)
                curr = curr.left

            # visit the next node in order, which is the most recently-added, aka smallest
            curr = stack.pop()
            k -= 1

            if k == 0:
                return curr.val
            
            curr = curr.right
        