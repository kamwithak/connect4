import random
import enum

class Empty(enum.Enum):
    EMPTY_SPACE = ''

class Player(enum.Enum):
    RANDOM_PLAYER = 'R'
    HUMAN_PLAYER = 'H'

class Connect4():
    def __init__(self, n=6, m=7, default_player=Player.HUMAN_PLAYER):
        self.n = n
        self.m = m
        self.board = self.create_board()
        self.current_player = default_player
        self.game_exit = False
        
    def print_board(self):
        for index, row in enumerate(self.board, start=1):
            print(f"{index} {[x.value for x in self.board[row]]}")

    def create_board(self):
        return {
            i : [Empty.EMPTY_SPACE for _ in range(self.m)] for i in range(self.n)
        }

    def verify_winner(self):
        # iterate over all rows
        for row_index in range(self.n):
            for col_index in range(self.m-3):
                if (self.board[row_index][col_index].value == self.current_player.value and \
                    self.board[row_index][col_index+1].value == self.current_player.value and \
                    self.board[row_index][col_index+2].value == self.current_player.value and \
                    self.board[row_index][col_index+3].value == self.current_player.value
                    ):
                    return True
        # iterate over all cols
        for row_index in range(self.n-3):
            for col_index in range(self.m):
                if (self.board[row_index][col_index].value == self.current_player.value and \
                    self.board[row_index+1][col_index].value == self.current_player.value and \
                    self.board[row_index+2][col_index].value == self.current_player.value and \
                    self.board[row_index+3][col_index].value == self.current_player.value
                    ):
                    return True
        # # iterate over downwards diagonals (L -> R)
        for row_index in range(self.n-3):
            for col_index in range(self.m-3):
                if (self.board[row_index][col_index].value == self.current_player.value and \
                    self.board[row_index+1][col_index+1].value == self.current_player.value and \
                    self.board[row_index+2][col_index+2].value == self.current_player.value and \
                    self.board[row_index+3][col_index+3].value == self.current_player.value
                    ):
                    return True
        # # iterate over upwards diagonals (L -> R)
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
        column_entry = ''
        while (not column_entry.isnumeric() or not (1 <= int(column_entry) <= 7)):
            column_entry = input("Please select a column between 1 and 7: ")
        return int(column_entry)
    
    def update_board(self, column_entry):
        row_of_interest = 0
        for row in self.board:
            possible_placement = self.board[row][column_entry-1]
            if (possible_placement.value != Empty.EMPTY_SPACE.value):
                break
            row_of_interest += 1
        if (row_of_interest == 0):
            return False
        self.board[row_of_interest-1][column_entry-1] = self.current_player
        return True

    def switch_players(self):
        if (self.current_player.value == Player.RANDOM_PLAYER.value):
            self.current_player = Player.HUMAN_PLAYER
        elif (self.current_player.value == Player.HUMAN_PLAYER.value):
            self.current_player = Player.RANDOM_PLAYER    

    def game_random_agent(self):
        print('Welcome to Connect4 - Practice Problem Edition!')
        while (not self.game_exit):
            print(f"Current player: {self.current_player}")
            print('~'*30)
            self.print_board()
            print('~'*30)
            if (self.current_player.value == Player.RANDOM_PLAYER.value):
                column_entry = random.randint(0, self.m)
            else:
                column_entry = self.request_move()
            successfully_updated = self.update_board(column_entry)
            if (not successfully_updated):
                continue
            if (self.verify_winner()):
                print('~'*30)
                self.print_board()
                print('~'*30)
                print(f"Winner: {self.current_player}")
                print('~'*30)
                self.game_exit = True
            self.switch_players()

if __name__ == '__main__':
    obj = Connect4()
    obj.game_random_agent()