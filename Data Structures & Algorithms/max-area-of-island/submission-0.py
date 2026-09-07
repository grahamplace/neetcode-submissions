class Solution:

    DIRS = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ]

    def processIsland(self, grid: list[list[int]], r: int, c: int) -> int:
        '''
        Process island from point r,c
        Process means we "fill" from that island point, erasing each visited value so we dont visit again
        return the area of the island
        '''
        # Out of bounds
        if (min(r, c) < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0): 
            return 0

        island_size = 1
        grid[r][c] = 0
        for dr, dc in self.DIRS:
            island_size += self.processIsland(grid, r + dr, c + dc)
        
        return island_size

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_area = max(max_area, self.processIsland(grid, r, c))
        
        return max_area