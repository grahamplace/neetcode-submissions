from collections import deque
from typing import List


class Solution:
    def processIsland(self, grid: List[List[str]], r: int, c: int) -> None:

        q = deque([(r, c)])
        grid[r][c] = "0"

        dirs = [
            (0, 1),
            (0, -1),
            (-1, 0),
            (1, 0),
        ]
        while q:
            cr, cc = q.popleft()
            for dr, dc in dirs:
                nr, nc = cr + dr, cc + dc
                if (
                    min(nr, nc) < 0
                    or nr >= len(grid)
                    or nc >= len(grid[0])
                    or grid[nr][nc] == "0"
                ):
                    continue

                q.append((nr, nc))
                grid[nr][nc] = "0"

    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    self.processIsland(grid, r, c)
                    island_count += 1

        return island_count