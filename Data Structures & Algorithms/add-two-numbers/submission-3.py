# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2, curr_new, new_head = l1, l2, None, None

        carryover = 0
        while curr1 or curr2 or carryover:
            total = carryover
            if curr1: total += curr1.val
            if curr2: total += curr2.val
            ones = total % 10
            carryover = total // 10

            new_node = ListNode(ones, None)

            if curr_new is None:
                new_head = new_node
                curr_new = new_head
            else:
                curr_new.next = new_node
                curr_new = curr_new.next

            if curr1: curr1 = curr1.next
            if curr2: curr2 = curr2.next
        
        return new_head
