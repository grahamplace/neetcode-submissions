from _heapq import heappush, heapify, heappop
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class HeapEntry:
    def __init__(self, node: ListNode):
        self.node = node
        self.val = node.val
    
    def __lt__(self, other_node: ListNode) -> bool:
        return self.val < other_node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        new_head_dummy = ListNode()
        new_list_curr = new_head_dummy
        
        # Build a min heap of the current head nodes
        head_heap = [HeapEntry(h) for h in lists if h]
        heapify(head_heap)

        while head_heap:
            curr = heappop(head_heap)
            new_list_curr.next = curr.node
            if curr.node.next:
                heappush(head_heap, HeapEntry(curr.node.next))
            
            new_list_curr = new_list_curr.next


        return new_head_dummy.next
        