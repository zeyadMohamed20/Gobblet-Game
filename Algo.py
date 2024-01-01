from TreeNode import TreeNode
from Board import Board
from cell import Player, _4th
import random
import time


time_limit_flag = False

def generate_random_integer():
    # Use the current time as a seed
    seed_value = int(time.time())
    random.seed(seed_value)

    # Generate a random integer in the range [0, 3]
    random_integer = random.randint(0, 3)

    return random_integer


def iterative_deepening(board, depth, maximizing_player, root_flag):
    global time_limit_flag
    global tic 
    time_limit_flag = False
    tic = time.perf_counter()
    temp_node = None
    for i in range(1, depth + 1):
        node = tree_expand(board, i)
        if time_limit_flag == False:
            temp_node = MiniMax(node, i, maximizing_player, root_flag)
        else:
            break
    return temp_node
    
def root_expand(root):
    if root.board.check_winner() != Player.NONE:
        return root
    for i in range(4):
        for j in range(4):
            if root.board.board_cells[i][j].owner == root.board.current_player:
                for k in range(4):
                    for l in range(4):
                        temp_board = Board(root.board)
                        new_board = temp_board
                        if new_board.move_gobblet(new_board.current_player, i, j, k, l):
                            new_board.play_next()
                            child = TreeNode(new_board)
                            root.add_child(child)

    for i in range(3):
        if root.board.current_player == Player.Black:
            if (i != 1 or (i == 1 and root.board.black_out_gobblets[i] != root.board.black_out_gobblets[i - 1])) and \
                    (i != 2 or (
                            i == 2 and root.board.black_out_gobblets[i] != root.board.black_out_gobblets[i - 1])) and \
                    (i != 2 or (i == 2 and root.board.black_out_gobblets[i] != root.board.black_out_gobblets[i - 2])):
                for k in range(4):
                    for l in range(4):
                        temp_board = Board(root.board)
                        new_board = temp_board
                        if new_board.board_add_gobblet(k, l, new_board.current_player, new_board.black_out_gobblets[i]):
                            new_board.play_next()
                            child = TreeNode(new_board)
                            root.add_child(child)
        else:
            if (i != 1 or (i == 1 and root.board.white_out_gobblets[i] != root.board.white_out_gobblets[i - 1])) and \
                    (i != 2 or (
                            i == 2 and root.board.white_out_gobblets[i] != root.board.white_out_gobblets[i - 1])) and \
                    (i != 2 or (i == 2 and root.board.white_out_gobblets[i] != root.board.white_out_gobblets[i - 2])):
                for k in range(4):
                    for l in range(4):
                        temp_board = Board(root.board)
                        new_board = temp_board
                        bit = new_board.white_out_gobblets[i]
                        if new_board.board_add_gobblet(k, l, new_board.current_player, bit):
                            new_board.play_next()
                            child = TreeNode(new_board)
                            root.add_child(child)

def tree_expand(board, depth):
    global time_limit_flag
    root = TreeNode(board)
    root_expand(root)
    if depth == 1:
        return root

    for i in range(len(root.children)):
        toc = time.perf_counter()
        print(f"{(toc - tic):0.4f}")
        if ((toc - tic) <= 15):
            root.children[i] = tree_expand(root.children[i].board, depth - 1)   
        else:
            time_limit_flag = True
            break

    return root

def bot_turn(board, difficulty, player):
    if not Board.flag:
        Board.flag = True
        row = generate_random_integer()
        col = generate_random_integer()
        board.board_add_gobblet(row, col, player, _4th)
        board.play_next()
        return board
    else:
        chosen_node = iterative_deepening(board, difficulty, player, True)
        return chosen_node.board