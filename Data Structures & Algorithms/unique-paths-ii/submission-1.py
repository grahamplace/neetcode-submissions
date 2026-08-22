from typing import Dict, Tuple, List

class Solution:

    def solve(self, obstacleGrid: List[List[int]], r: int, c: int, cache: Dict[Tuple[int, int], int]) -> int:
        # at position r, c:
        # Can move down or right UNLESS that position is blocked
        # base cases = blocked = 0 paths from there
        # bottom row and last col = 1 path from there (right, down)
        if r == len(obstacleGrid) - 1: 
            return 0 if any([v == 1 for v in obstacleGrid[r][c:]]) else 1
        if c == len(obstacleGrid[0]) - 1:
            obstacle = False
            for v in range(r, len(obstacleGrid)):
                if obstacleGrid[v][c] == 1:
                    obstacle = True
                    break
            return 0 if obstacle else 1
        if obstacleGrid[r][c] == 1: return 0
        if (r, c) in cache: return cache[(r, c)]

        down = self.solve(obstacleGrid, r + 1, c, cache)
        right = self.solve(obstacleGrid, r, c + 1, cache)
        cache[(r, c)] = down + right
        return cache[(r, c)] 


    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return self.solve(obstacleGrid, 0, 0, {})