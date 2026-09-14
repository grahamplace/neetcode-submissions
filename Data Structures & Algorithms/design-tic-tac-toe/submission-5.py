class TicTacToe:

    def __init__(self, n: int):
        self.board: list[list[int]] =[[0] * n for _ in range(n)]
        self.row_counters = [0 for _ in range(n)]
        self.col_counters = [0 for _ in range(n)]
        self.diag_dl_counter = 0
        self.diag_ur_counter = 0
        self.size = n

    def print_board(self):
        print("board", self.board)
        print("row_counters", self.row_counters)
        print("col_counters", self.col_counters)
        print("diag_dl_counter", self.diag_dl_counter)
        print("diag_ur_counter", self.diag_ur_counter)
        print("size", self.size)

    def update_counters(self, row, col, player) -> bool:
        player_value = -1 if player == 1 else 1

        self.row_counters[row] += player_value
        if abs(self.row_counters[row]) == self.size:
                return True

        self.col_counters[col] += player_value
        if abs(self.col_counters[col]) == self.size:
                return True

        if row == col:
            self.diag_dl_counter += player_value
            if abs(self.diag_dl_counter) == self.size:
                return True
        
        if row + col == self.size - 1:
            self.diag_ur_counter += player_value
            if abs(self.diag_ur_counter) == self.size:
                return True
        
        return False

    def move(self, row: int, col: int, player: int) -> int:

        # apply the move in the board data
        self.board[row][col] = player

        # update counters and check for any win condition post-move
        check = self.update_counters(row, col, player)
        # self.print_board()
        
        if check: return player
        
        return 0
        

# print("GP TEST")
# obj = TicTacToe(3)
# param_1 = obj.move(0,0,1)
# print("GP TEST DONE")

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
