from collections import deque

class Solution:

    DIRS = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]

    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()
        rotten = set()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    fresh.add((row, col))
                elif grid[row][col] == 2:
                    rotten.add((row, col))

        q = deque(rotten)
        ticks = 0
        while True:
            # TODO: end condition
            # TICK: expand from most recent set of rotten
            q_size = len(q)
            this_tick_new_rotten = set()
            for _ in range(q_size):
                cr, cc = q.popleft()

                for dr, dc in self.DIRS:
                    nr = cr + dr
                    nc = cc + dc
                    # bounds checks / already visited
                    if min(nr, nc) < 0 or nr >= len(grid) or nc >= len(grid[0]) or (nr, nc) in rotten:
                        continue
                    if grid[nr][nc] == 1: # neighbor of rotten is fresh
                        this_tick_new_rotten.add((nr, nc))

            if len(this_tick_new_rotten) == 0:
                return -1 if len(fresh) > 0 else ticks
            
            for new_rot in this_tick_new_rotten:
                fresh.remove(new_rot)
                rotten.add(new_rot)
                q.append(new_rot)
            
            ticks += 1

        return ticks