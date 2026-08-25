'''
Given numbers 
- numbers
- already sorted in non-decreasing (so duplicates allowed?)
- e.g. [1,2,3,4], 


OUTPUT
- 1 INDEXED indices
- of 2 elems that add up to target
- AND index1 < index 2 (NOT equal, can't use self + self)

CONSTRAINTS 
- O(1) additional space.
- There will always be exactly ONE valid solution
- input has at least 2 elems, no empty checks needed
- negative numbers ARE allowed

IDEA
- Sliding Window, start at min + max (0, last)
- if sum of those is too big: no solution
- if sum is too small: move the pointer that max the minimum change in sum 
- converge on solution 
- if pointers ever cross or ==, no solution (can't use same elem twice)
- O(n)


WALKTHROUGH
t = 5 [-5, -3, 0, 2, 4, 6, 8]
[-5L, -3, 0, 2, 4, 6, 8R] => 3
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            curr = numbers[left] + numbers[right]

            if curr == target:
                return [left + 1, right + 1]

            # if curr is < target, we would only want to increase the sum (incr left)
            if curr < target: 
                left += 1
            
            # if curr is > target, we would only want to increase the sum (incr left)
            if curr > target: 
                right -= 1

        
        # should never happen if we have valid inputs
        assert False, "Unexpectedly reached end of twoSum!"
        return [-1, -1]





        