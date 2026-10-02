"""
Notes
- Best not to iterate over sparse grid, wasteful
- Ideally, we have O(1) lookups of cell positions (get 1, 2)
  - And some set of fresh fruit
- each pass = walk over all fresh pos, check neighbors for any rotten
- NOTE: the entire tick happens at once, don't make a fresh fruit rotten mid-turn
"""

class Solution:
    def doesFreshRot(self, rotten, fresh_pos):
        DIRS = [
            (0,-1), # LEFT
            (0,1), # RIGHT
            (1, 0), # DOWN 
            (-1,0), # UP
        ]

        for dx, dy in DIRS:
            if (fresh_pos[0] + dx, fresh_pos[1] + dy) in rotten:
                return True

    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh: set[tuple[int, int]] = set()
        rotten: set[tuple[int, int]] = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                elif grid[i][j] == 2:
                    rotten.add((i, j))
        
        minutes = 0
        while fresh:
            now_rotten = set()
            for fresh_pos in fresh:
                if self.doesFreshRot(rotten, fresh_pos):
                    now_rotten.add(fresh_pos)
            
            # apply newly-rotten
            for newly_rotten_pos in now_rotten:
                fresh.remove(newly_rotten_pos)
                rotten.add(newly_rotten_pos)

            # handle case where a fresh fruit cannot be reached by any rotten, impossible, return -1            
            if len(now_rotten) == 0 and len(fresh) > 0:
                return -1

            minutes += 1

        return minutes