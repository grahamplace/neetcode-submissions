class TicTacToe:

    def __init__(self, n: int):
        self.board: list[list[int]] =[[0] * n for _ in range(n)]

    def check_win(self, row: int, col: int, player: int) -> bool:        
        row_win = True
        for row_value in self.board[row]:
            if row_value != player:
                row_win = False
                break

        col_win = True
        for col_value in [r[col] for r in self.board]:
            if col_value != player:
                col_win = False
                break
        
        diag_dl_win = False
        diag_ur_win = False
        if row == col: # diag down left
            diag_dl_win = True
            for i in range(len(self.board)):
                if self.board[i][i] != player:
                    diag_dl_win = False
                    break
        
        if row + col == len(self.board) - 1: # diag down right
            diag_ur_win = True
            for i in range(len(self.board)):
                i_col = len(self.board) - i - 1
                if self.board[i][i_col] != player:
                    diag_ur_win = False
                    break


        return any([
            row_win, 
            col_win,
            diag_dl_win,
            diag_ur_win,
        ])


    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        # check for win after move is made:
        if self.check_win(row, col, player):
            return player

        return 0
        

# print("GP TEST")
# obj = TicTacToe(3)
# param_1 = obj.move(0,0,1)
# print("GP TEST DONE")

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
