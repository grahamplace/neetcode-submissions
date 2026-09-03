# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Given LL head of len n
n is ALWAYS even
list[i] is the TWIN of list[n - 1 - i]
 - if i <= (n / 2) - 1

basically for the first half of the list?

ex: [5,4,2,1]
n = 4 
(n / 2) - 1 ==> 1
so possible i values w/ twins are 0, 1 (first half)

i = 0
twin is n - 1 - i ==> 3 (1 val)

i = 1 
twin is n - 1 - i ==> 2 (2 val)

Want:
MAX twin sum

The twin sum is defined as the sum of a node and its twin.


Problem:
we only have head, don't actually know n

idea: 
run a pointer to midpoint of list (fast / slow)
We could keep a stack but that creates o(n) space
if we split the lists and reverse the second half, then we just do two pointers over both lists

'''
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        midpoint = slow
        print(f"slow: {midpoint.val}")
        prev = None
        curr = slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        reversed_head = prev


        curr_a, curr_b, max_twin_sum = head, reversed_head, 0
        while True:
            if curr_a == midpoint:
                break
            
            max_twin_sum = max(max_twin_sum, curr_a.val + curr_b.val)
            curr_a = curr_a.next 
            curr_b = curr_b.next


        return max_twin_sum
