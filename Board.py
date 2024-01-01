# Commit Message: Initialize Board Class with Constructor
# Initial setup of the Board class, including the constructor and instance variables.
# Handles the initialization of the game board, out gobblet arrays, and current player.
# Defines methods for moving gobblets, adding gobblets to the board, and checking validity.

from cell import Cell, Player, _4th
import copy

class Board:
    def __init__(self, board1=None):
        if board1 is None:
            self.flag_add = None  # True if add, False if move
            self.curr_stack = -1  # if add, store current number of stack
            self.curr_size = -1   # if add, store current gobblet size
            self.curr_row = -1    # if add, store destination row
            self.curr_col = -1    # if add, store destination col
            self.from_row = -1    # if move, store source row
            self.from_col = -1    # if move, store source col
            self.to_row = -1      # if move, store destination row
            self.to_col = -1      # if move, store destination col

            self.white_out_gobblets = [_4th, _4th, _4th]
            self.black_out_gobblets = [_4th, _4th, _4th]
            self.board_cells = [[Cell() for _ in range(4)] for _ in range(4)]
            self.current_player = Player.White
        else:
            # Deep copy to maintain separate instances
            self.white_out_gobblets = copy.deepcopy(board1.white_out_gobblets)
            self.black_out_gobblets = copy.deepcopy(board1.black_out_gobblets)
            self.board_cells = copy.deepcopy(board1.board_cells)
            self.current_player = copy.deepcopy(board1.current_player)

            # Copy additional flags for game state
            self.flag_add = board1.flag_add
            self.curr_stack = board1.curr_stack
            self.curr_size = board1.curr_size
            self.curr_row = board1.curr_row
            self.curr_col = board1.curr_col
            self.from_row = board1.from_row
            self.from_col = board1.from_col
            self.to_row = board1.to_row
            self.to_col = board1.to_col
            
    # checks if there are 4 cells of the same color on the same row colomn or diagonal
    flag = False
    def check_winner(self):
        for i in range(4):
            if all(cell.owner == Player.Black for cell in self.board_cells[i]):
                return Player.Black
            elif all(cell.owner == Player.White for cell in self.board_cells[i]):
                return Player.White

        for j in range(4):
            if all(self.board_cells[i][j].owner == Player.Black for i in range(4)):
                return Player.Black
            elif all(self.board_cells[i][j].owner == Player.White for i in range(4)):
                return Player.White

        if all(self.board_cells[i][i].owner == Player.Black for i in range(4)):
            return Player.Black
        elif all(self.board_cells[i][i].owner == Player.White for i in range(4)):
            return Player.White
        if all(self.board_cells[i][abs(3 - i)].owner == Player.Black for i in range(4)):
            return Player.Black
        elif all(self.board_cells[i][abs(3 - i)].owner == Player.White for i in range(4)):
            return Player.White

        return Player.NONE
        
    # changes current player
    def play_next(self):
        self.current_player = Player.White if self.current_player == Player.Black else Player.Black
    
    # move gobblet by removing it from a cell and put it in another cell
    def move_gobblet(self, player, row_from, column_from, row_to, column_to):
        size = self.get_gobblet_size(row_from, column_from)

        if (self.board_cells[row_to][column_to].check_validity(size) and self.board_cells[row_from][column_from].remove_gobblet(player, size)):
            self.board_cells[row_to][column_to].add_gobblet(player, size)
            self.flag_add = False
            self.to_row = row_to
            self.to_col = column_to
            self.from_row = row_from
            self.from_col = column_from
            return True
        else:
            return False
