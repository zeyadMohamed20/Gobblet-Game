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