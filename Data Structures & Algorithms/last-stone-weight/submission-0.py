from heapq import heapify, heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * s for s in stones]
        heapify(stones)

        while len(stones) > 1:
            y = -1 * heappop(stones)
            x = -1 * heappop(stones)

            if x < y:
                heappush(stones, -1 * (y - x))
        
        return 0 if len(stones) == 0 else -1 * stones[-1]