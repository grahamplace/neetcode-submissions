class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0,0,0]
        for n in nums:
            counts[n] += 1
        
        
        i = 0
        for j, c in enumerate(counts):
            for _ in range(c):
                nums[i] = j
                i += 1