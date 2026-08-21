from typing import Optional

class MyNode:
    def __init__(self, value: int, next_node: Optional["MyNode"]):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return f"value: {self.value}, next_node: {self.next_node}"

class MyLinkedList:

    def __init__(self):
        self.head: Optional[MyNode] = None
        self.tail: Optional[MyNode] = None
        self.size = 0

    def __str__(self) -> str:
        return f"head: {self.head}, tail: {self.tail}, size: {self.size}"

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        for _ in range(index):
            assert curr is not None
            curr = curr.next_node
        
        assert curr is not None
        return curr.value

    def addAtHead(self, val: int) -> None:
        new_node = MyNode(val, self.head)
        self.head = new_node
        self.size += 1

        if self.size == 1:
            self.tail = new_node

        return 

    def addAtTail(self, val: int) -> None:
        new_node = MyNode(val, None)

        if self.tail is not None:
            self.tail.next_node = new_node
            self.tail = new_node
        
        else: # empty case
            self.head = new_node
            self.tail = new_node

        self.size += 1
        return


    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size: 
            return
        if index == 0: 
            self.addAtHead(val)
            return 
        if index == self.size: 
            return self.addAtTail(val)

        # a -> b -> d
        # want pointer at b so I can insert by updating b.next
        # insert at 2 to get a b c d 
        prev = self.head
        for _ in range(index - 1):
            assert prev is not None
            prev = prev.next_node
        
        assert prev is not None
        prev.next_node = MyNode(val, prev.next_node)
        self.size += 1
        


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        # single-node case 
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0 
            return

        
        prev = self.head
        for _ in range(index - 1):
            assert prev is not None
            prev = prev.next_node
        
        assert prev is not None

        # delete tail case
        if index == self.size - 1:
            prev.next_node = None
            self.tail = prev
        else: # delete middle case 
            assert prev.next_node
            prev.next_node = prev.next_node.next_node

        self.size -= 1

        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)