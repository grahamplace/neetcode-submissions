"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

'''

Process root:
 create edges to each neighbor in orig nodes set
 but what if neighbor not in copy set yet?
   -> process neighbor first, recursive?
   -> 

'''

from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        new_head = Node(node.val)
        old_to_new_map = {node: new_head}
        old_nodes_q = deque([node])
        while old_nodes_q:
            
            curr_old = old_nodes_q.popleft()
            curr_new = old_to_new_map[curr_old]

            for child in curr_old.neighbors:
                if child not in old_to_new_map: 
                    new_node = Node(child.val)
                    old_to_new_map[child] = new_node
                    old_nodes_q.append(child)
            
                curr_new.neighbors.append(old_to_new_map[child])

        return new_head

