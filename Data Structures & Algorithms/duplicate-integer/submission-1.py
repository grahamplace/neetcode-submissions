class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums: 
            return False
            
        return max(Counter(nums).values()) > 1