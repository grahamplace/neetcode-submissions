class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_seen = 0

        left = 0 
        right = len(heights) - 1

        while left < right:
            curr = (right - left) * min(heights[left], heights[right])
            max_seen = max(curr, max_seen)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_seen