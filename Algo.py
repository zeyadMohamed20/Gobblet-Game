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
def MiniMax(node, depth, maximizing_player, root_flag):
    res_node = node
    if depth == 0 or node.board.check_winner() == maximizing_player:
        return node

    if maximizing_player == Player.Black:
        max_eval = float('-inf')
        for child in node.children:
            x_node = MiniMax(child, depth - 1, Player.White, False)
            eval_val = x_node.Value
            if eval_val > max_eval:
                max_eval = eval_val
                res_node = x_node
                node.Value = max_eval
        if root_flag:
            return res_node
        else:
            return node
    elif maximizing_player == Player.White:
        min_eval = float('inf')
        for child in node.children:
            x_node = MiniMax(child, depth - 1, Player.Black, False)
            eval_val = x_node.Value
            if eval_val < min_eval:
                min_eval = eval_val
                res_node = x_node
                node.Value = min_eval
        if root_flag:
            return res_node
        else:
            return node
        
def minimax_with_alphabeta(node, depth, maximizing_player, root_flag):
    res_node = node
    if depth == 0:
        node.alpha = node.Value
        node.beta = node.Value
        return node
    if maximizing_player == Player.Black:
        for child in node.children:
            child_node = minimax_with_alphabeta(child, depth - 1, Player.White, False)
            if child_node.beta > node.alpha:
                node.alpha = child_node.beta
                res_node = child_node
            if node.beta <= node.alpha:
                break
    elif maximizing_player == Player.White:
        for child in node.children:
            child_node = minimax_with_alphabeta(child, depth - 1, Player.Black, False)
            if child_node.alpha < node.beta:
                node.beta = child_node.alpha
                res_node = child_node
            if node.beta <= node.alpha:
                break

    if root_flag:
        return res_node
    else:
        return node

