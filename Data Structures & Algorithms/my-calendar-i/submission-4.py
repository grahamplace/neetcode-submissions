from dataclasses import dataclass

@dataclass
class TreeNode:
    start: int
    end: int
    left: "TreeNode | None"
    right: "TreeNode | None"

class MyCalendar:
    
    def __init__(self):
        self.head = None

    def _do_nodes_overlap(self, a: TreeNode, b: TreeNode) -> bool:
        # (1, 5) (10, 15)
        if a.end <= b.start or b.end <= a.start:
            return False
        
        # (1, 10)  (2, 5)
        if b.start >= a.start and b.end <= a.end:
            return True

        # (2, 5) (1, 10) 
        if a.start >= b.start and a.end <= b.end:
            return True

        # (1, 5) (2, 10) 
        if b.start >= a.start and a.end < b.end:
            return True

        # (1, 5) (2, 10) 
        if a.start >= b.start and b.end < a.end:
            return True

        return False


    def book(self, startTime: int, endTime: int) -> bool:

        assert self._do_nodes_overlap(TreeNode(1, 5, None, None), TreeNode(2, 3, None, None)) == True
        assert self._do_nodes_overlap(TreeNode(1, 5, None, None), TreeNode(5, 6, None, None)) == False
        assert self._do_nodes_overlap(TreeNode(1, 5, None, None), TreeNode(6, 9, None, None)) == False
        assert self._do_nodes_overlap(TreeNode(1, 5, None, None), TreeNode(2, 10, None, None)) == True
        assert self._do_nodes_overlap(TreeNode(5, 6, None, None), TreeNode(1, 5, None, None)) == False
        assert self._do_nodes_overlap(TreeNode(1, 10, None, None), TreeNode(5, 11, None, None)) == True


        if self.head is None:
            self.head = TreeNode(startTime, endTime, None, None)
            return True

        curr = self.head 
        while curr:
            print(curr.start, curr.end)
            if self._do_nodes_overlap(curr,  TreeNode(startTime, endTime, None, None)):
                return False
            
            if startTime < curr.start:
                if curr.left is None:
                    curr.left = TreeNode(startTime, endTime, None, None)
                    return True
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = TreeNode(startTime, endTime, None, None)
                    return True
                curr = curr.right

        return True

        

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)