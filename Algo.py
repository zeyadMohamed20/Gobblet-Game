from TreeNode import TreeNode
from Board import Board
from cell import Player, _4th
import random
import time


time_limit_flag = False


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