from typing import Dict
class Solution:
    def _rob(self, nums: List[int], i: int, cache: Dict[int, int]):
        if i >= len(nums):
            return 0
        
        if i in cache:
            return cache[i]

        # at any index, we choose to rob this house or the next house
        # we then follow that choice path all the way recursively, and pick the best pick
        this_house = nums[i] + self._rob(nums, i + 2, cache)
        next_house = self._rob(nums, i + 1, cache)
        cache[i] = max(this_house, next_house)
        return cache[i]

    def rob(self, nums: List[int]) -> int:
        # conceptually: we always rob one of the last two (or one of the first two?)
        # otherwise you are just leaving money on the table
        # ideas: backtracking? (choice = house 1 or house 2, then continue down that path)
        # depth first search, walk all paths from root -> leaves when you reach a leaf check vs max seen and update
        # BU DFS-like tree walk but with DP? working backwards from end we don't need to recompute paths
        # TD DFS? recursive + memoization?
        return self._rob(nums, 0, {})