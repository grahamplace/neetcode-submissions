from collections import deque

class Solution:
    def backtrack(self, nums: list, path: list, solutions: list[list]):
        if not nums:
            solutions.append(list(path))
            return


        # choices here are:
        # (a) skip this num
        # (b) take this num

        # choose
        chose_curr = nums[0]
        path.append(chose_curr)

        # explore with path if we take
        self.backtrack(nums[1:], path, solutions)

        # unchoose
        path.pop()

        # explore with path if we skip
        self.backtrack(nums[1:], path, solutions)


    def subsets(self, nums: List[int]) -> List[List[int]]:
       solutions = []
       self.backtrack(nums, [], solutions)
       return solutions