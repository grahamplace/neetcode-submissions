# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Basic idea: 
Level order traversal of graph (LL)
Keep a hashset of Seen 
if we ever visit a node which we have seen before, that's a cycle
(because each node can only have one child, there are NOT multiple paths to any node)
- We don't actually have to do a queue for level-order traversal since there is only one possible child per node
'''

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        curr = head 
        while curr:
            if curr in seen:
                return True

            seen.add(curr)
            curr = curr.next
        
        return False








