"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def traverse_to_min(self, node: 'Node') -> 'Node':
        curr = node
        while curr.left:
            curr = curr.left
        
        return curr

    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if node.right:
            return self.traverse_to_min(node.right)
        
        target = node.val
        curr = node
        while curr.parent:
            curr = curr.parent
            if curr.val > target:
                return curr