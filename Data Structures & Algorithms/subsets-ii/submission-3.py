class Solution:

    def explore(self, nums: list, i: int, path: list, solutions: list):
        if i >= len(nums):
            solutions.append(list(path))
            return

        # choices here are SKIP ALL REPEATS or TAKE FIRST
        path.append(nums[i]) # Take first
        self.explore(nums, i + 1, path, solutions)
        path.pop()

        j = i
        while j + 1 < len(nums) and nums[j] == nums[j + 1]:
            j += 1
        
        self.explore(nums, j + 1, path, solutions)


    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutions = []
        self.explore(nums, 0, [], solutions)
        return solutions