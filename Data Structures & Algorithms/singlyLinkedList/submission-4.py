from typing import List, Optional


class Node:
    def __init__(self, val: int, next_node: Optional["Node"] = None):
        self.value = val
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        i = 0

        while curr:
            if i == index:
                return curr.value

            curr = curr.next_node
            i += 1

        return -1

    def insertHead(self, val: int) -> None:
        new_head = Node(val, self.head)
        self.head = new_head

    def insertTail(self, val: int) -> None:
        new_node = Node(val)

        # Empty list
        if self.head is None:
            self.head = new_node
            return

        curr = self.head
        while curr.next_node:
            curr = curr.next_node

        curr.next_node = new_node

    def remove(self, index: int) -> bool:
        # Empty list
        if self.head is None:
            return False

        # Removing the head
        if index == 0:
            self.head = self.head.next_node
            return True

        # Find the node before the one to remove
        prev = self.head
        i = 0

        while i < index - 1 and prev.next_node:
            prev = prev.next_node
            i += 1

        # The target node does not exist
        if prev.next_node is None:
            return False

        # Remove the target node
        prev.next_node = prev.next_node.next_node
        return True

    def getValues(self) -> List[int]:
        values = []
        curr = self.head

        while curr:
            values.append(curr.value)
            curr = curr.next_node

        return values
