from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        
        L = 0 

        window = set()
        for R in range(len(nums)):
            # initial window-fill up:
            if R <= k:
                if nums[R] in window: return True
                window.add(nums[R])
                continue
            else:
                window.remove(nums[L])
                if nums[R] in window:
                    return True
                else:
                    window.add(nums[R])
                L += 1
        
        return False
