class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_streak = 0
        current_max = 0

        for i in range(len(nums) + 1):
            if  i == len(nums) or nums[i] == 0:
                current_max = max(current_max, current_streak)
                current_streak = 0
            else:
                current_streak += 1
        
        return current_max