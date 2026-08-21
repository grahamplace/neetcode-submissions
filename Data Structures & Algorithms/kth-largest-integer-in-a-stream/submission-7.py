from heapq import heappush, heappop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_k_heap = []
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:

        # if our minKHeap is not full yet, we can just blindly push
        if len(self.min_k_heap) < self.k:
            heappush(self.min_k_heap, val)
            return self.min_k_heap[0]

        curr_min = heappop(self.min_k_heap)
        
        if curr_min < val:
            heappush(self.min_k_heap, val)
        else:
            heappush(self.min_k_heap, curr_min)

        return self.min_k_heap[0]

        