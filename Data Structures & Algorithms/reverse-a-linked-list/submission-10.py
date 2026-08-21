# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # solve it recursively for practice:
        # a -> b -> c 

        # reverse(a -> b -> c )
        # same as reverse(a.next) -> a
        # base case is tail, aka no next on head

        if head is None or head.next is None:
            return head
        else:
            sub_list = self.reverseList(head.next) # c -> b
            # head: a -> b (at this point)
            # want: a -> none, b -> a

            head.next.next = head
            head.next = None
            return sub_list
