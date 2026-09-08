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








