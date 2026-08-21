class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        newHead = None
        currNew = None
        curr1 = list1 
        curr2 = list2 


        while curr1 and curr2:
            if (curr1.val <= curr2.val):
                if not currNew:
                    newHead = curr1
                    currNew = newHead
                    curr1 = curr1.next
                else:
                    currNew.next = curr1
                    curr1 = curr1.next
                    currNew = currNew.next

            else:
                if not currNew:
                    newHead = curr2
                    currNew = newHead
                    curr2 = curr2.next
                else:
                    currNew.next = curr2
                    curr2 = curr2.next
                    currNew = currNew.next

        if currNew and curr1: currNew.next = curr1
        if currNew and curr2: currNew.next = curr2

        return newHead