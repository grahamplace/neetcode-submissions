from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1
            
        q = deque([(0,0)])
        seen = {(0, 0)}
        distance = 0
        dirs = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]
        while q:            
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == rows - 1 and c == cols - 1:
                    return distance

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (
                        nr < 0 or nr >= rows or
                        nc < 0 or nc >= cols or
                        (nr, nc) in seen or
                        grid[nr][nc] == 1
                    ):
                        continue

                    seen.add((nr, nc))
                    q.append((nr, nc))

            distance += 1
        
        return -1