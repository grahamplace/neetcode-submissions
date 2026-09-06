class Solution:
    DIRS = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]

    def _explore(
        self, board: list[list[str]], r: int, c: int, word: str, visited: set[tuple[int, int]]
    ) -> bool:
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
            return False

        if (r, c) in visited:
            return False

        if len(word) == 1 and board[r][c] == word:
            return True

        if board[r][c] == word[0]:
            visited.add((r, c))
            for dr, dc in self.DIRS:
                nr = r + dr
                nc = c + dc
                if (nr, nc) not in visited and self._explore(board, nr, nc, word[1:], visited):
                    return True
            visited.remove((r, c))

        return False

    def exist(self, board: list[list[str]], word: str) -> bool:
        for r in range(len(board)):
            for c in range(len(board[0])):
                if self._explore(board, r, c, word, set()):
                    return True

        return False
