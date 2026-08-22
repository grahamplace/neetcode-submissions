from typing import Dict, Tuple

class Solution:
    def solve(self, r: int, c: int, m: int, n: int, cache: Dict[Tuple[int, int], int]) -> int:
        if r == m - 1 and c == n - 1:
            return 1

        if r > m or c > n:
            return 0
        
        if (r, c) in cache:
            return cache[(r, c)]
        
        down_paths = self.solve(r + 1, c, m, n, cache)
        right_paths = self.solve(r, c + 1, m, n, cache)
        cache[(r, c)] = down_paths + right_paths
        return cache[(r, c)]

    def uniquePaths(self, m: int, n: int) -> int:
        return self.solve(0, 0, m, n, {})