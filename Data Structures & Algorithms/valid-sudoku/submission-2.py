"""
INPUTS
9 x 9 Sudoku board board
- size is always valid

OUTPUTS
- true/false if board is valid:
- Each row must contain the digits 1-9 without duplicates
- Each column must contain the digits 1-9 without duplicates
- Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates
"""

from collections import defaultdict
from typing import List


class Solution:
    def isValidRow(self, board: List[List[str]], r: int, cache):
        if r in cache:
            return True

        row = board[r]
        seen = set()
        for v in row:
            if v != "." and v in seen:
                return False
            else:
                seen.add(v)

        cache.add(r)
        return True

    def isValidCol(self, board: List[List[str]], c: int, cache):
        if c in cache:
            return True

        seen = set()
        for _, row in enumerate(board):
            v = row[c]
            if v != "." and v in seen:
                return False
            else:
                seen.add(v)

        cache.add(c)
        return True

    def isValidSubGrid(self, board: List[List[str]], r: int, c: int, cache) -> bool:
        # anchor each point to the origin (top left) point of its subgrid
        sub_row = (r // 3) * 3
        sub_col = (c // 3) * 3
        if (sub_row, sub_col) in cache:
            return True

        seen = set()
        dirs = [
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 0),
            (1, 1),
            (1, 2),
            (2, 0),
            (2, 1),
            (2, 2),
        ]
        for d in dirs:
            v = board[sub_row + d[0]][sub_col + d[1]]
            if v != "." and v in seen:
                return False
            else:
                seen.add(v)

        cache.add((sub_row, sub_col))
        return True

    def solvePoint(
        self, board: List[List[str]], r: int, c: int, row_cache, col_cache, sub_cache
    ) -> bool:
        return (
            self.isValidRow(board, r, row_cache)
            and self.isValidCol(board, c, col_cache)
            and self.isValidSubGrid(board, r, c, sub_cache)
        )

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_cache = set()
        col_cache = set()
        sub_cache = set()
        for r in range(len(board)):
            for c in range(len(board[r])):
                if not self.solvePoint(board, r, c, row_cache, col_cache, sub_cache):
                    return False

        return True
