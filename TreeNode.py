from Board import Board
from cell import Player
import copy


class TreeNode:
    # constructor, it copies the tree from another one, it changes cell values if they are changed by providing the
    # new value,row,column
    def __init__(self, board1: Board, cell=None, row=None, col=None, cell2=None, row2=None, col2=None):
        self.board = copy.deepcopy(Board(board1))
        self.Value = 0
        self.alpha = float('-inf')
        self.beta = float('inf')
        self.children = []
        self.board.black_out_gobblets = copy.deepcopy(board1.black_out_gobblets)
        self.board.white_out_gobblets = copy.deepcopy(board1.white_out_gobblets)
        if cell is not None and row is not None and col is not None:
            self.board.board_cells[row][col] = copy.deepcopy(cell)

        if cell2 is not None and row2 is not None and col2 is not None:
            self.board.board_cells[row2][col2] = copy.deepcopy(cell2)

        self.calc_value()

    # add child to children array
    def add_child(self, child):
        self.children.append(child)

    def calc_value(self):
        self.Value = 0
        # increase value according to number of owned cell and it's gobblet size
        for i in range(4):
            for j in range(4):
                if self.board.board_cells[i][j].owner == Player.Black:
                    self.Value += self.board.board_cells[i][j].get_gobblet_size()
                elif self.board.board_cells[i][j].owner == Player.White:
                    self.Value -= self.board.board_cells[i][j].get_gobblet_size()

        for i in range(4):
            black_count = 0
            white_count = 0

            for j in range(4):
                if self.board.board_cells[i][j].owner == Player.Black:
                    black_count += 1
                elif self.board.board_cells[i][j].owner == Player.White:
                    white_count += 1
            # add value according to number of owned cells in rows
            if black_count >= 3:
                self.Value += 100
            elif white_count >= 3:
                self.Value -= 100
            elif black_count == white_count:
                self.Value += 0
            elif black_count == 2:
                self.Value += 50
            elif white_count == 2:
                self.Value -= 50
            if black_count > 3:
                self.Value += 10000

            elif white_count > 3:
                self.Value -= 10000

            if black_count == 3 and white_count == 1:
                self.Value -= 500
            elif white_count == 3 and black_count == 1:
                self.Value += 500

            black_count = 0
            white_count = 0
            # add value according to number of owned cells in colomn
            for j in range(4):
                if self.board.board_cells[j][i].owner == Player.Black:
                    black_count += 1
                elif self.board.board_cells[j][i].owner == Player.White:
                    white_count += 1

            if black_count >= 3:
                self.Value += 100
            elif white_count >= 3:
                self.Value -= 100

            elif black_count == white_count:
                self.Value += 0
            elif black_count == 2:
                self.Value += 50
            elif white_count == 2:
                self.Value -= 50
            if black_count > 3:
                self.Value += 10000

            elif white_count > 3:
                self.Value -= 10000

            if black_count == 3 and white_count == 1:
                self.Value -= 500
            elif white_count == 3 and black_count == 1:
                self.Value += 500
        black_count = 0
        white_count = 0
        for j in range(4):
            if self.board.board_cells[j][j].owner == Player.Black:
                black_count += 1
            elif self.board.board_cells[j][j].owner == Player.White:
                white_count += 1
        if black_count >= 3:
            self.Value += 100
        elif white_count >= 3:
            self.Value -= 100
        elif black_count == white_count:
            self.Value += 0
        elif black_count == 2:
            self.Value += 50
        elif white_count == 2:
            self.Value -= 50
        if black_count > 3:
            self.Value += 10000

        elif white_count > 3:
            self.Value -= 10000

        if black_count == 3 and white_count == 1:
            self.Value -= 500
        elif white_count == 3 and black_count == 1:
            self.Value += 500

        black_count = 0
        white_count = 0
        for j in range(4):
            if self.board.board_cells[j][abs(j - 3)].owner == Player.Black:
                black_count += 1
            elif self.board.board_cells[j][abs(j - 3)].owner == Player.White:
                white_count += 1
        if black_count >= 3:
            self.Value += 100
        elif white_count >= 3:
            self.Value -= 100
        elif black_count == white_count:
            self.Value += 0
        elif black_count == 2:
            self.Value += 50
        elif white_count == 2:
            self.Value -= 50
        if black_count > 3:
            self.Value += 10000

        elif white_count > 3:
            self.Value -= 10000

        if black_count == 3 and white_count == 1:
            self.Value -= 500
        elif white_count == 3 and black_count == 1:
            self.Value += 500
    