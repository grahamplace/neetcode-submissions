from collections import deque

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # do it with backtracking WITHOUT creating a tree in memory:
        if len(nums) == 0:
            return []

        solution = []

        def explore(depth: int, path: List[int]): 

            if depth == len(nums):
                solution.append(path)
                return
            
            explore(depth + 1, path + [nums[depth]]) # with this num included
            explore(depth + 1, path) # without this num included

        explore(0, [])
        return solution
