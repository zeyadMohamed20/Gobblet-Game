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

