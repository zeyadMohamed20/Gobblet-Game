# Gobblet-Game
CSE472s Artificial Intelligence Course Project. This project is about implementing the game-playing of Gobblet, Gobblet game is an abstract game played on a 4x4 grid with each of the two players having twelve pieces that can nest on top of one another to create three stacks of four pieces.

1-We implemented the tree expansion functions which generates all possible moves for thegiven board and if the depth is more than one then it will generate all the possible moves of the children and so on. These functions are used by the game playing algorithms where they evealute the generated tree nodes and determine the best move possible.
	
2-we also implemented the function of the bot_turn in which the bot calls the gameplaying algorithm which calls the tree expansion function.