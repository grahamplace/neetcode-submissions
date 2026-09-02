class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = None
        for L in range(len(nums)):
            curr_sum = nums[L]
            if curr_sum >= target: 
                return 1
                
            R = L + 1
            while R < len(nums):
                curr_sum += nums[R]
                if curr_sum >= target:
                    min_length = R - L + 1 if not min_length else min(min_length, R - L + 1)
                    break # continuing for this L has no point

                R += 1

        return min_length if min_length else 0
            