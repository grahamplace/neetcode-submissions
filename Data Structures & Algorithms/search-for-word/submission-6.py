class Solution:
    DIRS = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]


    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def _explore(board: list[list[str]], r: int, c: int, index: int, visited: set[tuple[int, int]]
        ) -> bool:
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or (r, c) in visited
                or board[r][c] != word[index]
            ):
                return False

            if index == len(word) - 1:
                return True

            if board[r][c] == word[index]:
                visited.add((r, c))
                for dr, dc in self.DIRS:
                    nr = r + dr
                    nc = c + dc
                    if _explore(board, nr, nc, index + 1, visited):
                        return True
                visited.remove((r, c))

            return False

        for r in range(rows):
            for c in range(cols):
                if _explore(board, r, c, 0, set()):
                    return True

        return False
