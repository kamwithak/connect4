from enum import Enum

class Player(Enum):
    RED_PLAYER = 'RED'
    YELLOW_PLAYER = 'YELLOW'

class Connect4():
    def __init__(self, n=6, m=7, default_player=Player.RED_PLAYER):
        self.n = n
        self.m = m
        self.board = self.create_board()
        self.default_player = default_player

    def print_board(self):
        print(self.board)

    def create_board(self):
        board = {i : ['EMPTY' for _ in range(self.m)] for i in range(self.n)}
        # board[5] = [Player.RED_PLAYER, Player.RED_PLAYER, Player.RED_PLAYER, Player.RED_PLAYER, -1, -1 ,-1]
        return board

    def getRows(self):
        return self.board[0], self.board[1], self.board[2], self.board[3], self.board[4], self.board[5]

    def verify_winner(self, winner):    
        # iterate over all rows
        for row_index in self.board:
            row = self.board[row_index]
            i = 0
            for j in range(3, self.m):
                if (all(isinstance(entry, type(winner)) for entry in row[i:j+1])):
                    return True
                i += 1
        # iterate over all cols
        row1, row2, row3, row4, row5, row6 = self.getRows()
        for col in zip(row1, row2, row3, row4, row5, row6):
            col = list(col)
            i = 0
            for j in range(3, self.n):
                if (all(isinstance(entry, type(int)) for entry in col[i:j+1])):
                    return True
                i += 1
        # iterate over downwards diagonals (L -> R)
        for row_index in range(self.n-3):
            for col_index in range(self.m-3):
                if (isinstance(self.board[row_index][col_index], type(winner)) & \
                    isinstance(self.board[row_index+1][col_index+1], type(winner)) & \
                    isinstance(self.board[row_index+2][col_index+2], type(winner)) & \
                    isinstance(self.board[row_index+3][col_index+3], type(winner))):
                    return True
        # iterate over upwards diagonals (L -> R)
        for row_index in range(self.n-3):
            for col_index in range(3, self.m):
                if (isinstance(self.board[row_index][col_index], type(winner)) & \
                    isinstance(self.board[row_index-1][col_index+1], type(winner)) & \
                    isinstance(self.board[row_index-2][col_index+2], type(winner)) & \
                    isinstance(self.board[row_index-4][col_index+4], type(winner))):
                    return True
        return False
    
    def game_engine(self):
        pass



if __name__ == '__main__':
  obj = Connect4()
  print(obj.create_board())
  print(obj.verify_winner(Player.RED_PLAYER))