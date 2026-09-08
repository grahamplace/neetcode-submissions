# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
"good" if the path from the root of the tree to the node x contains no nodes with a value greater than the value of node x

so - from node, traversing up to root, if we ever see a node w value > curr value, not good
or - from root, if we knew the max above curr, we would know if there are greater values or not


DFS / backtracking style solution
visit each node, check if good/if max needs to be updated 
visit children with new max 

return the number of good nodes within the tree
'''
class Solution:

    def _goodNodes(self, root: TreeNode, max_along_branch: int | None) -> int:
        count = 0

        count += 1 if max_along_branch is None or root.val >= max_along_branch else 0

        new_max = root.val if max_along_branch is None else max(max_along_branch, root.val)
        if root.left:
            count += self._goodNodes(root.left, new_max)
        
        if root.right:
            count += self._goodNodes(root.right, new_max)

        return count

        

    def goodNodes(self, root: TreeNode) -> int:
        return self._goodNodes(root, None)