# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



'''
basic idea:
- k-size queue (stack) where k = n input (for better naming)
- as we iterate through list, keep the last k elems we've seen
- each elem = append new to queue, dequeue one

iterate over entire list
when we reach the end, the next element to dequeue is the nth from end that we want to delete, so we can get it in O(1)
'''
from collections import deque

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        q = deque()
        curr = head 
        while curr:
            # keep at most k + 1 elems in q
            if len(q) == n + 1:
                q.popleft()
            q.append(curr)
            curr = curr.next

        # Case 1: deleting head 
        # deleting e.g. the 2nd (n=2) from a 2-elem array == deleting head
        if len(q) == n:
            # to delete the head, just return the head's next as new head
            return head.next

        # Case 2: deleting middle/tail
        parent = q.popleft()
        to_delete = q.popleft()
        parent.next = to_delete.next

        return head

        