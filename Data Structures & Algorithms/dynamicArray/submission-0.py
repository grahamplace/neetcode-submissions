from typing import List, Optional

from types import NoneType
class DynamicArray:
    '''
    Under the hood, dynamic array uses a linked list 
    '''
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be > 0")

        self._array: List[Optional[int]] = [None for _ in range(capacity)]
        self._size = 0
        self._capacity = capacity


    def get(self, i: int) -> int:
        ret_val = self._array[i]
        if type(ret_val) == NoneType:
            raise ValueError(f"unexpected i: {i}")

        return ret_val


    def set(self, i: int, n: int) -> None:
        self._array[i] = n
        return 

    def pushback(self, n: int) -> None:
        new_size = self._size + 1
        if new_size > self._capacity:
            self.resize()
        
        self.set(new_size - 1, n)
        self._size = new_size
        return


    def popback(self) -> int:
        ret_val = self.get(self._size - 1)
        self._array[self._size - 1] = None
        self._size -= 1 
        return ret_val

    def resize(self) -> None:
        tmp = self._array
        new_capacity = len(tmp) * 2
        self._array = [None for _ in range(new_capacity)]
        self._capacity = new_capacity
        for idx, e in enumerate(tmp):
            self._array[idx] = e
        
        return

    def getSize(self) -> int:
        return self._size
    
    def getCapacity(self) -> int:
        return self._capacity
