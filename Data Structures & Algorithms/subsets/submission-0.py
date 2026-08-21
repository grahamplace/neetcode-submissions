from typing import List, Optional, Self
from collections import deque

class Node:
    def __init__(self, value: List[int], left: Optional[Self], right: Optional[Self]):
        self.value = value
        self.left = left
        self.right = right

class Tree:
        def __init__(self):
            self.root: Optional[Node] = Node([], None, None)

        # level order traversal (breadth first)
        def get_leaves(self) -> List[Node]:            
            if not self.root: return []

            leaves = []
            q = deque([self.root])

            while len(q) > 0:
                curr = q.popleft()
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)

                if not curr.left and not curr.right:
                    leaves.append(curr)
                    
            return leaves

        def insert(self, val: int) -> None:
            leaves = self.get_leaves()
            for leaf in leaves:
                leaf.left = Node(list(leaf.value) + [val], None, None) # include num path 
                leaf.right = Node(list(leaf.value), None, None) # skip num path



class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Construct tree:
        tree = Tree()
        for num in nums: 
            tree.insert(num)
        
        return [l.value for l in tree.get_leaves()]

