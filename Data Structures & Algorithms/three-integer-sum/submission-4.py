class Solution:

    def threeSum(self, nums: List[int]) ->  List[List[int]]:
        nums.sort()
        solution = []

        for i in range(len(nums) - 2):
            if nums[i] > 0: # if known-smallest is >0, no solution 
                 break
                
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum < 0:
                    left += 1
                elif curr_sum > 0:
                    right -= 1
                else:
                    solution.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1


        return solution
        
