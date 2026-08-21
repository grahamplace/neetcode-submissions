class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # counts = [0,0,0]
        # for n in nums:
        #     counts[n] += 1
        
        
        # i = 0
        # for j, c in enumerate(counts):
        #     for _ in range(c):
        #         nums[i] = j
        #         i += 1


        # Dutch national flag one-pass: 
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
            elif nums[mid] == 1:
                mid += 1
            
