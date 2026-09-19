from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # counts = Counter(nums)
        # return [k for k, v in counts.items() if v == 1][0]
        
        curr = nums[0]
        for i in range(1, len(nums)):
            curr = curr ^ nums[i]

        return curr