# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        # Add a dummy before head to simplify head delete edge case
        dummy = ListNode(-1, head)
        left: ListNode = dummy 
        right: ListNode = dummy
        for _ in range(n):
            right = right.next

        while right.next:
            left = left.next 
            right = right.next
        
        left.next = left.next.next

        return dummy.next # throw out the dummy we added 

        