class Solution:
    DIRS = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]


    def exist(self, board: list[list[str]], word: str) -> bool:
        def _explore(board: list[list[str]], r: int, c: int, start_idx: int, visited: set[tuple[int, int]]
        ) -> bool:
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False

            if (r, c) in visited:
                return False

            if start_idx == len(word) - 1 and board[r][c] == word[-1]:
                return True

            if board[r][c] == word[start_idx]:
                visited.add((r, c))
                for dr, dc in self.DIRS:
                    nr = r + dr
                    nc = c + dc
                    if _explore(board, nr, nc, start_idx + 1, visited):
                        return True
                visited.remove((r, c))

            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if _explore(board, r, c, 0, set()):
                    return True

        return False
