class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        solutions = []

        def explore(self, i, path, current_sum):

            if i >= len(nums):
                return

            # choice 1, pick this number
            new_sum = current_sum + nums[i]
            path.append(nums[i])

            if new_sum == target: # if choosing this # hits target, add a solution
                solutions.append(path.copy())
            elif new_sum < target:  # if choosing this # keeps new sum under target, we are within a valid path, continue exploring
                explore(self, i, path, new_sum)

            # choice 2, skip this number
            # Undo choice so we can try "skip this number" paths
            path.pop()
            explore(self, i + 1, path, current_sum)

        explore(self, 0, [], 0)

        return solutions
