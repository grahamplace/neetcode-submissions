# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Postorder = L, R, N 
    '''
    def _postorderTraversal(self, root: Optional[TreeNode], output: list[int]) -> list[int]:
        if not root: return output
        self._postorderTraversal(root.left, output)
        self._postorderTraversal(root.right, output)
        output.append(root.val)
        return output


    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self._postorderTraversal(root, [])

        # output = []
        # stack = [root]
        # curr = root

        # while curr or stack:
        #     if curr is None:
        #         curr = stack.pop()
        #         output.append(curr.val)
        #     else:
        #         stack.append(curr.left)
        #         stack.append(curr.right)
        #         curr = curr.left

        # return output