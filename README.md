# Pong with Reinforcement Learning

## SnakeCore.py

Core logic of the game, SnakeVisual is only a demo for visualization. A single SankeCore object can be viewed as a one game round.

<span style="color:red">**random.seed(1) keeps every game the same, remove before actual use**</span>

### reset_gameboard(x, y)

Generates a new game board matrix of size x+2, y+2. -2 is filled around the edge for easier collision detection. Randomly spawn head within 1 blocks range of the edge. Randomly spawn first food (different from head position). Randomize initial direction.

### snake_move(direction)

direction can be one of the following lists or "None": ["x", 1] ["x", -1] ["y", 1] ["y", -1]

If a 180 deg turn is given, snake moves in previous direction.

If None is given, snake moves in previous direction.

snake_move returns True if move is completed, False if snake: 1. hits body  2. hits boundary  3. fills the entire board

### spawn_food()

Iterates through the matrix, records all positions with 0.

Randomly picks a valid postion and spawn food (set value to -1).