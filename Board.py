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
        # Check rows
        for i in range(4):
            if all(cell.owner == Player.Black for cell in self.board_cells[i]):
                return Player.Black
            elif all(cell.owner == Player.White for cell in self.board_cells[i]):
                return Player.White
    
        # Check columns
        for j in range(4):
            if all(self.board_cells[i][j].owner == Player.Black for i in range(4)):
                return Player.Black
            elif all(self.board_cells[i][j].owner == Player.White for i in range(4)):
                return Player.White
    
        # Check main diagonal
        if all(self.board_cells[i][i].owner == Player.Black for i in range(4)):
            return Player.Black
        elif all(self.board_cells[i][i].owner == Player.White for i in range(4)):
            return Player.White
    
        # Check other diagonal
        if all(self.board_cells[i][abs(3 - i)].owner == Player.Black for i in range(4)):
            return Player.Black
        elif all(self.board_cells[i][abs(3 - i)].owner == Player.White for i in range(4)):
            return Player.White
    
        # If no winner is found
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
            
    # add gobblet to a cell in the board but first check if it is valid to take this gobblet from out stacks
    def board_add_gobblet(self, row, column, player, bit):
        # Check the validity of the move using board_check_validity method
        flag = self.board_check_validity(row, column, player, bit)
    
        # If the move is not valid, return False
        if not flag:
            return False
    
        # Check if the target cell is occupied by the opponent's gobblet
        if self.board_cells[row][column].owner != player and self.board_cells[row][column].owner != Player.NONE:
            rows = 0
            columns = 0
            diagonal = 0
    
            # Check the number of opponent's gobblets in the same row
            for i in range(4):
                if self.board_cells[row][i].owner != player and self.board_cells[row][i].owner != Player.NONE:
                    rows = rows + 1
    
                # Check the number of opponent's gobblets in the same column
                if self.board_cells[i][column].owner != player and self.board_cells[i][column].owner != Player.NONE:
                    columns = columns + 1
    
            # Check the number of opponent's gobblets in the main diagonal
            if row == column:
                for i in range(4):
                    if self.board_cells[i][i].owner != player and self.board_cells[i][i].owner != Player.NONE:
                        diagonal = diagonal + 1
    
            # Check the number of opponent's gobblets in the secondary diagonal
            if row + column == 3:
                for i in range(4):
                    if self.board_cells[i][3-i].owner != player and self.board_cells[i][3-i].owner != Player.NONE:
                        diagonal = diagonal + 1
    
            # If there are three opponent's gobblets in a row, column, or diagonal, return False
            if rows == 3 or columns == 3 or diagonal == 3:
                return False
    
        # Set flag_add to True, indicating a successful addition of a gobblet
        self.flag_add = True
        # Record the current row and column for reference
        self.curr_row = row
        self.curr_col = column
    
        # Determine the current player's stack, size, and update the corresponding out gobblet
        if player == Player.Black:
            for i in range(3):
                if self.black_out_gobblets[i] == bit:
                    self.curr_stack = i
                    self.curr_size = bit
                    self.black_out_gobblets[i] = self.black_out_gobblets[i] >> 1
                    self.board_cells[row][column].add_gobblet(player, bit)
                    break
        else:
            for i in range(3):
                if self.white_out_gobblets[i] == bit:
                    self.curr_stack = i
                    self.curr_size = bit
                    self.white_out_gobblets[i] = self.white_out_gobblets[i] >> 1
                    self.board_cells[row][column].add_gobblet(player, bit)
                    break
    
        # Return True to indicate a successful move
        return True
        
    # Introduce Player-Controlled Gobblet Addition    
    def player_add_gobblet(self, row, column, player, bit, index):
        # Check the validity of the move using board_check_validity method
        flag = self.board_check_validity(row, column, player, bit)
    
        # If the move is not valid, return False
        if not flag:
            return False
    
        # Check if the target cell is occupied by the opponent's gobblet
        if self.board_cells[row][column].owner != player and self.board_cells[row][column].owner != Player.NONE:
            rows = 0
            columns = 0
            diagonal = 0
    
            # Check the number of opponent's gobblets in the same row
            for i in range(4):
                if self.board_cells[row][i].owner != player and self.board_cells[row][i].owner != Player.NONE:
                    rows = rows + 1
    
                # Check the number of opponent's gobblets in the same column
                if self.board_cells[i][column].owner != player and self.board_cells[i][column].owner != Player.NONE:
                    columns = columns + 1
    
            # Check the number of opponent's gobblets in the main diagonal
            if row == column:
                for i in range(4):
                    if self.board_cells[i][i].owner != player and self.board_cells[i][i].owner != Player.NONE:
                        diagonal = diagonal + 1
    
            # Check the number of opponent's gobblets in the secondary diagonal
            if row + column == 3:
                for i in range(4):
                    if self.board_cells[i][3-i].owner != player and self.board_cells[i][3-i].owner != Player.NONE:
                        diagonal = diagonal + 1
    
            # If there are three opponent's gobblets in a row, column, or diagonal, return False
            if rows == 3 or columns == 3 or diagonal == 3:
                temp = True
            else:
                return False
    
        # If the player is Black, update Black's out gobblets and add the gobblet to the board
        if player == Player.Black:
            self.black_out_gobblets[index] = self.black_out_gobblets[index] >> 1
            self.board_cells[row][column].add_gobblet(player, bit)
        # If the player is White, update White's out gobblets and add the gobblet to the board
        else:
            self.white_out_gobblets[index] = self.white_out_gobblets[index] >> 1
            self.board_cells[row][column].add_gobblet(player, bit)
    
        # Return True to indicate a successful move
        return True    
        
    # check if there is a gobblet of the same size in the outside stacks, and also the cell validity
    def board_check_validity(self, row, column, player, bit):
        if not self.board_cells[row][column].check_validity(bit):
            return False

        # Iterate through the player's out gobblets to check if the specified bit matches any of them
        for i in range(3):
            # Check for White player's out gobblets
            if player == Player.White:
                if self.white_out_gobblets[i] == bit:
                    # Return True if the bit matches one of White's out gobblets
                    return True
            # Check for Black player's out gobblets
            elif player == Player.Black:
                if self.black_out_gobblets[i] == bit:
                    # Return True if the bit matches one of Black's out gobblets
                    return True
        
        # Return False if the specified bit does not match any of the player's out gobblets
        # or if the target cell is not valid for placing a gobblet of the specified size
        return False

    def get_gobblet_size(self, row, column):
        if self.board_cells[row][column]:
            return self.board_cells[row][column].get_gobblet_size()

        return None

    def Draw(self):
        for i in range(4):
            for j in range(4):
                if self.board_cells[i][j].owner == Player.White:
                    print("White", self.get_gobblet_size(i, j), "\t", end="")
                elif self.board_cells[i][j].owner == Player.Black:
                    print("Black", self.get_gobblet_size(i, j), "\t", end="")
                else:
                    print("NONE", end="\t")
            print("\n")
        print("BLACK OUT: ", end="")
        for i in range(3):
            print(self.black_out_gobblets[i], end="\t")
        print("\n")

        print("White OUT: ", end="\t")
        for i in range(3):
            print(self.white_out_gobblets[i], end="\t")
        print("\n")

        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
