from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        L = 0
        R = min(k + 1, len(nums))
        curr_window = defaultdict(int)

        for i in range(L, R):
            if nums[i] in curr_window: 
                return True

            curr_window[nums[i]] += 1

        while R < len(nums):
            curr_window[nums[L]] -= 1
            curr_window[nums[R]] += 1
            if curr_window[nums[R]] > 1:
                return True

            R += 1
            L += 1
        
        return False
