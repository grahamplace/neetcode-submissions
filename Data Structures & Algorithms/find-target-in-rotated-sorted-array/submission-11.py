'''
- Given an array of length n
- It was originally sorted in ascending order
- It has now been rotated between 1 and n times 
- [1,2,3,4,5,6] rotated 4 times = [3,4,5,6,1,2]

INPUTS
- nums: rotated sorted array 
- target: integer

OUTPUT
- index of `target` within `nums`
- -1 if it is not present.

CONSTRAINTS
- You may assume all elements in the sorted rotated array nums are unique
- 1 <= nums.length <= 1000 - less than 1k numbers in input
-1000 <= nums[i] <= 1000 - each num is between 
  * CAN BE NEGATIVE
-1000 <= target <= 1000
  * CAN BE NEGATIVE
- All values of nums are unique
- nums is an ascending array that is possibly rotated.
  * nums ALREADY SORTED (ish)
- ? are nums a sequence? 1, 2, 3 etc or just sorted ints?


REQUIREMENTS
- O(n) time is trivial, can you write an algorithm that runs in O(log n) time?
'''
from typing import List

class Solution:

    def find_min(self, nums: List[int], left: int, right: int):
        while left < right:
            midpoint = left + (right - left) // 2
            if nums[midpoint] > nums[right]:
                left = midpoint + 1
            else:
                right = midpoint
            
        return left

    def _binary_search(self, nums: List[int], target: int, left: int, right: int) -> int:        
        while left <= right:
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            
        return -1 

    def search(self, nums: List[int], target: int) -> int:
        shift = self.find_min(nums, 0, len(nums) - 1)

        # nums is two sorted arrays, the right one starts at shift location (min value)
        if nums[shift] <= target <= nums[-1]:
            return self._binary_search(nums, target, shift, len(nums) - 1)
        else:
            # the left one is 0 : shift idx - 1
            return self._binary_search(nums, target, 0, shift - 1)
