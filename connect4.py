import sys
from enum import Enum

class Empty(Enum):
    EMPTY_SPACE = 'EMPTY'

class Player(Enum):
    RED_PLAYER = 'RED'
    YELLOW_PLAYER = 'YELLOW'

class Connect4():
    def __init__(self, n=6, m=7, default_player=Player.YELLOW_PLAYER):
        self.n = n
        self.m = m
        self.board = self.create_board()
        self.current_player = default_player
        self.game_exit = False
        
    def print_board(self):
        for index, row in enumerate(self.board, start=1):
            print(index, self.board[row])

    def create_board(self):
        return {
            i : [Empty.EMPTY_SPACE for _ in range(self.m)] for i in range(self.n)
        }

    def verify_winner(self):    
        # iterate over all rows
        for row_index in range(self.n):
            for col_index in range(self.m-4):
                if (self.board[row_index][col_index].value == self.current_player.value and \
                    self.board[row_index][col_index+1].value == self.current_player.value and \
                    self.board[row_index][col_index+2].value == self.current_player.value and \
                    self.board[row_index][col_index+3].value == self.current_player.value
                    ):
                    return True
        # iterate over all cols
        for row_index in range(self.n):
            for col_index in range(self.m-4):
                if (self.board[col_index][row_index].value == self.current_player.value and \
                    self.board[col_index+1][row_index].value == self.current_player.value and \
                    self.board[col_index+2][row_index].value == self.current_player.value and \
                    self.board[col_index+3][row_index].value == self.current_player.value
                    ):
                    return True
        # iterate over downwards diagonals (L -> R)
        for row_index in range(self.n-3):
            for col_index in range(self.m-3):
                if (self.board[row_index][col_index].value == self.current_player.value and \
                    self.board[row_index+1][col_index+1].value == self.current_player.value and \
                    self.board[row_index+2][col_index+2].value == self.current_player.value and \
                    self.board[row_index+3][col_index+3].value == self.current_player.value
                    ):
                    return True
        # iterate over upwards diagonals (L -> R)
        for row_index in range(self.n-3):
            for col_index in range(3, self.m):
                if (self.board[row_index][col_index].value == self.current_player.value and \
                    self.board[row_index+1][col_index-1].value == self.current_player.value and \
                    self.board[row_index+2][col_index-2].value == self.current_player.value and \
                    self.board[row_index+3][col_index-3].value == self.current_player.value
                    ):
                    return True
        return False
    
    def request_move(self):
        column_entry = input("Please select a column between 1 and 7")
        if (not (column_entry.isnumeric() and 1 <= int(column_entry) <= 7)):
            self.request_move()
        return int(column_entry)
    
    def update_board(self, column_entry):
        row_of_interest = 0
        for row in self.board:
            possible_placement = self.board[row][column_entry-1]
            if (possible_placement.value != Empty.EMPTY_SPACE.value):
                break
            row_of_interest += 1
        self.board[row_of_interest-1][column_entry-1] = self.current_player

    def switch_players(self):
        if (self.current_player.value == Player.RED_PLAYER.value):
            self.current_player = Player.YELLOW_PLAYER
        elif (self.current_player.value == Player.YELLOW_PLAYER.value):
            self.current_player = Player.RED_PLAYER    

    def game_engine(self):
        print('Welcome to Connect4 - Practice Problem Edition!')
        while (not self.game_exit):
            print(f"Current player: {self.current_player}")
            self.print_board()
            column_entry = self.request_move()
            self.update_board(column_entry)
            if (self.verify_winner()):
                print('~'*25)
                self.print_board()
                print(f"Winner: {self.current_player}")
                self.game_exit = True
            else:
                self.switch_players()

if __name__ == '__main__':
    obj = Connect4()
    obj.game_engine()
    sys.exit()