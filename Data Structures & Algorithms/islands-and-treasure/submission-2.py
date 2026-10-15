# find all treasure chests
# from each, BFS outward (only expanding to land)
# if land cell and current is SMALLER distance, stop
# if land cell at current distance is LARGER (worse solution), set to our distance and keep expanding
# we can set the land cells to distances since pos = land. and inf is WORSE than curr distance
class Solution:
    DIRS = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ]


    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        treasure_chests = []
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0: 
                    treasure_chests.append((row, col))

        q: deque[tuple[int, int]] = deque(treasure_chests)
        distance_from_chest = 0
        seen: set[tuple[int, int]] = set(treasure_chests)
        while q:
            level_size = len(q)
            for _ in range(level_size):
                cr, cc = q.popleft()
                if min(cr, cc) < 0 or cr >= len(grid) or cc >= len(grid[cr]) or grid[cr][cc] < 0: # TODO: = 0?
                    continue

                if grid[cr][cc] > 0 and grid[cr][cc] > distance_from_chest:
                    grid[cr][cc] = distance_from_chest

                for dr, dc in self.DIRS:
                    n = (cr + dr, cc + dc)
                    if n not in seen:
                        q.append(n)
                        seen.add(n)

            distance_from_chest += 1
    

