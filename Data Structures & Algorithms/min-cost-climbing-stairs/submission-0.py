class Solution:
    def _calc(self, cost: list[int], idx: int, cache: dict[int, int]) -> int:
        if idx in cache: 
            return cache[idx]

        if idx == len(cost):
            cache[idx] = 0
            return 0
        
        if idx >= len(cost) - 2:
            cache[idx] = cost[idx]
            return cost[idx] # optimal for last two steps is always pay this cost and then be done

        one_step = self._calc(cost, idx + 1, cache)
        two_step = self._calc(cost, idx + 2, cache)
        min_path_from_idx = cost[idx] + min(one_step, two_step)
        cache[idx] = min_path_from_idx
        return min_path_from_idx


    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return self._calc([0] + cost, 0, {})