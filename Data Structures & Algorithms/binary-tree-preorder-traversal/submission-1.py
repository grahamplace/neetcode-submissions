# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def _preorderTraversal(self, root: Optional[TreeNode], output: list[int]) -> List[int]:
    #     if root is None:
    #         return output

    #     output.append(root.val)
    #     self._preorderTraversal(root.left, output)
    #     self._preorderTraversal(root.right, output)
    #     return output
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        output = []
        curr = None
        while curr or stack:
            if curr is None:
                curr = stack.pop()
            else:
                output.append(curr.val)
                if curr.right: stack.append(curr.right)
                curr = curr.left

        return output

        
        