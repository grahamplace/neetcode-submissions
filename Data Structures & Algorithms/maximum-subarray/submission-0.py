class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_seen = nums[0] # subarray len 1, valid
        curr_sum = 0
        for num in nums:
            # before adding curr, check (?reset) curr_sum
            curr_sum = max(curr_sum, 0)
            curr_sum += num
            max_seen = max(max_seen, curr_sum)
            
        return max_seen