class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        L, R = 0, len(nums) - 1
        while L < R:
            if nums[L] < nums[R]:
                return nums[L]
            mid = (L + R) // 2

            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid
        
        return nums[L]