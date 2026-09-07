class Solution:
    DIRS = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ]

    def processIsland(self, grid: list[list[int]], r: int, c: int, visited: set) -> int:
        if (
            min(r, c) < 0
            or r >= len(grid)
            or c >= len(grid[0])
            or grid[r][c] == 0
            or (r, c) in visited
        ):
            return 0

        island_size = 1
        visited.add((r, c))
        for dr, dc in self.DIRS:
            island_size += self.processIsland(grid, r + dr, c + dc, visited)

        return island_size

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_area = max(max_area, self.processIsland(grid, r, c, visited))

        return max_area
