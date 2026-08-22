from typing import List, Optional, Tuple

class HashTable:
    def __init__(self, capacity: int):
        self._array: List[List[Tuple[int, int]]] = [[] for _ in range(capacity)]
        self._size = 0

    def _hash(self, key: int) -> int:
        return key % self.getCapacity()

    def _insert(self, key: int, value: int) -> None:
        # key is present, delete old before adding new k/v to chain
        if self.get(key) != -1:
            chain = self._array[self._hash(key)]
            for idx, v in enumerate(chain):
                if v[0] == key:
                    del chain[idx]
                    self._size -= 1

        self._array[self._hash(key)].append((key, value))
        self._size += 1

    def insert(self, key: int, value: int) -> None:
        self._insert(key, value)

        # resize when 50% full
        if self._size / self.getCapacity() >= 0.5:
            self.resize()

        return

    def get(self, key: int) -> int:
        chain = self._array[self._hash(key)]
        for v in chain:
            if v[0] == key: return v[1]

        return -1

    def remove(self, key: int) -> bool:
        result = self.get(key)
        if result != -1:
            chain = self._array[self._hash(key)]
            for idx, v in enumerate(chain):
                if v[0] == key:
                    del(chain[idx])
                    self._size -= 1
                    return True
        
        return False

    def getSize(self) -> int:
        return self._size

    def getCapacity(self) -> int:
        return len(self._array)

    def resize(self) -> None:
        new_capacity = 2 * self.getCapacity()
        old_items = []
        for chain in self._array:
            old_items.extend(chain)

        self._array = [[] for _ in range(new_capacity)]
        self._size = 0

        for o in old_items:
            self._insert(o[0], o[1])
