# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return head

        slow = head 
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head_b = slow.next
        slow.next = None

        prev = None
        while head_b:
            next_node = head_b.next
            head_b.next = prev
            prev = head_b
            head_b = next_node
        
        head_b = prev

        curr_a = head
        curr_b = head_b
        while curr_a and curr_b:
            tmp_a = curr_a.next
            tmp_b = curr_b.next
            curr_a.next = curr_b
            curr_b.next = tmp_a
            curr_a = tmp_a
            curr_b = tmp_b
        
        curr = head
        while curr:
            print(curr.val)
            curr = curr.next
