class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        newHead = None
        currNew = None

        while list1 and list2:

            if list1.val <= list2.val:  # l1 is smaller, add l1 to new list
                if not currNew: # empty new list case, set up new list
                    newHead = list1
                    currNew = newHead
                else:
                    currNew.next = list1
                    currNew = currNew.next  # advance currNew 

                list1 = list1.next # advance l1 pointer, since we just used one if it's values

            else: # l2 is smaller, add l2 to new list
                if not currNew:
                    newHead = list2 
                    currNew = newHead
                
                else:
                    currNew.next = list2
                    currNew = currNew.next
                
                list2 = list2.next # advance l2 pointer, since we just used one if it's values

        
        if not currNew:
            return None
        
        if list1: currNew.next = list1
        if list2: currNew.next = list2

        return newHead