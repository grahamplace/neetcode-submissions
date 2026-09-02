class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sums = [0]
        for n in nums:
            prefix_sums.append(prefix_sums[-1] + n)
        

        postfix_sums = [0]
        j = len(nums) - 1
        while j >= 0:
            postfix_sums.append(postfix_sums[-1] + nums[j])
            j -= 1
        
        postfix_sums.reverse()

        print(prefix_sums, postfix_sums)
        for i in range(1, len(nums) + 1):
            print(i, prefix_sums[i], postfix_sums[i - 1])
            if prefix_sums[i] == postfix_sums[i - 1]:
                return i - 1
            
        return -1
        