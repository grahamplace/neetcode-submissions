from collections import deque

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solution = []

        def explore(depth: int, path: List[int]): 

            if depth == len(nums):
                solution.append(list(path))
                return
            
            path.append(nums[depth])
            explore(depth + 1, path) # with this num included
            
            path.pop()
            explore(depth + 1, path) # without this num included

        explore(0, [])
        return solution
