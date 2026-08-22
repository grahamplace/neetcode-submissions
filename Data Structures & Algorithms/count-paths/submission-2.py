from typing import Dict, Tuple

class Solution:
    # Memoized Solution
    # def solve(self, r: int, c: int, m: int, n: int, cache: Dict[Tuple[int, int], int]) -> int:
    #     if r == m - 1 and c == n - 1:
    #         return 1

    #     if r > m or c > n:
    #         return 0
        
    #     if (r, c) in cache:
    #         return cache[(r, c)]
        
    #     down_paths = self.solve(r + 1, c, m, n, cache)
    #     right_paths = self.solve(r, c + 1, m, n, cache)
    #     cache[(r, c)] = down_paths + right_paths
    #     return cache[(r, c)]

    def uniquePaths(self, m: int, n: int) -> int:
        # BUP DP Solution:
        # At [-1][-1] (target destination), there is 1 valid path
        # Left and above that, there is 1 valid path
        # in each cell of last row, there is 1 valid path (right move is only option)
        # our dp state = one row
        # we build the row above that row from right to left, using the "cache" from row below (precomputed) and cell to right (just computed)
        # at the end we return the first cell of last (top) row, that's the origin point 

        row_below = [1 for _ in range(n)]
        r = m - 1

        while r > 0:
            curr_row: List[int] = [-1 for _ in range(n)]
            curr_row[-1] = 1 # the rightmost col can ONLY go straight down
            for c in range(n - 2, -1, -1): # start at second-from-right col to avoid boundary issues
                # compute and cache curr cell at (r, c)
                down_opt = row_below[c]
                right_opt = curr_row[c + 1]
                assert right_opt != -1, "Something went wrong!"
                curr_row[c] = down_opt + right_opt
            
            row_below = curr_row.copy()
            r -= 1
        
        return row_below[0]