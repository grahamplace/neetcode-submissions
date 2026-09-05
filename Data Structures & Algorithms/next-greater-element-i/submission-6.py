class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_map = {val: idx for idx, val in enumerate(nums2)}
        stack = []
        next_greater = [-1] * len(nums2)
        for idx, n2 in enumerate(nums2):
            while stack and nums2[stack[-1]] < n2:
                popped = stack.pop()
                next_greater[popped] = n2
            
            stack.append(idx)

        return [next_greater[nums2_map[n]] for n in nums1]