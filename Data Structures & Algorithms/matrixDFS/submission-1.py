class Solution:
    def dfs(self, grid: List[List[int]], r: int, c: int, seen: set) -> int:
        if r == len(grid) - 1 and c == len(grid[0]) - 1:
            return 1

        seen.add((r, c))
        dirs = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]

        paths = 0
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if (
                (nr, nc) in seen
                or min(nr, nc) < 0
                or nr >= len(grid)
                or nc >= len(grid[0])
                or grid[nr][nc] == 1
            ):
                continue
            
            paths += self.dfs(grid, nr, nc, seen)
        
        seen.remove((r, c))
            
        return paths

    def countPaths(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0

        return self.dfs(grid, 0, 0, set())
