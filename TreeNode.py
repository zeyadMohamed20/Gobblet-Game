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

    