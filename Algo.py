from TreeNode import TreeNode
from Board import Board
from cell import Player, _4th
import random
import time


def generate_random_integer():
    # Use the current time as a seed
    seed_value = int(time.time())
    random.seed(seed_value)

    # Generate a random integer in the range [0, 3]
    random_integer = random.randint(0, 3)

    return random_integer

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

