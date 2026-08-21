class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        currA = list1
        currB = list2
        currHead = None
        currNew = None

        while currA and currB:
            if currA.val <= currB.val:
                if not currHead:
                    currHead = currA
                else:
                    currNew.next = currA
                currNew = currA
                currA = currA.next
            else:
                if not currHead:
                    currHead = currB
                else:
                    currNew.next = currB
                currNew = currB
                currB = currB.next
                
        if currA: currNew.next = currA
        if currB: currNew.next = currB

        return currHead