# Gobblet-Game
CSE472s Artificial Intelligence Course Project. This project is about implementing the game-playing of Gobblet, Gobblet game is an abstract game played on a 4x4 grid with each of the two players having twelve pieces that can nest on top of one another to create three stacks of four pieces.

1-We implemented the gameplaying algorithms which are MinMax algorithm and Minmax with alpha beta pruning and iterative deepening with alpha beta pruning.

2-These algorithms are used to evaluate a tree and return the best possible move but the depth of the given tree determines the level of goodness.

3-We also added a time constraint heuristic to limit the move of the Bot where it does not exceed 3 miniutes of playing and if it is violated it will return the best move already reached by the previous level(depth)