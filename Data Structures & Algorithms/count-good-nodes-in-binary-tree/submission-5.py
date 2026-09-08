# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        count = 0 
        stack: list[tuple[TreeNode, int]] = [(root, root.val)]

        while stack:
            curr, max_so_far = stack.pop()

            if curr.val >= max_so_far:
                count += 1

            new_max = max(max_so_far, curr.val)

            if curr.left: stack.append((curr.left, new_max))
            if curr.right: stack.append((curr.right, new_max))

        return count








