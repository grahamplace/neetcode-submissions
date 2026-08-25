'''
FIFO: [1] [1, 2]
MIN:  [1] [1, 1]
'''


from typing import Optional, List 


class MinStack:

    def __init__(self):
        self._stack: List[int] = []
        self._min_stack: List[int] = [] 
        self.size: int = 0

    def push(self, val: int) -> None:
        self._stack.append(val)
        min_at_val_insert = min(self._min_stack[-1], val) if self._min_stack else val
        self._min_stack.append(min_at_val_insert)
        self.size += 1

    def pop(self) -> None:
        self._stack.pop()
        self._min_stack.pop()
        self.size -= 1

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        # inputs don't specify how to handle this case
        if len(self._min_stack) == 0:
            return -1

        return self._min_stack[-1]
