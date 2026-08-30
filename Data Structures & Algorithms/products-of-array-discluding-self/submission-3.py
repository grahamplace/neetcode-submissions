class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array = [1]
        for n in range(1, len(nums)):
            prefix_array.append(nums[n - 1] * prefix_array[n - 1])
        
        suffix_array = [1]
        s_i = 1
        for n in range(len(nums), 1, -1):
            suffix_array.append(nums[n - 1] * suffix_array[s_i - 1])
            s_i += 1
        suffix_array.reverse()

        return [prefix_array[i] * suffix_array[i] for i in range(len(suffix_array))]
