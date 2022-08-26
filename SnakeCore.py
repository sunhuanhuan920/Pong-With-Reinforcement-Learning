import numpy as np
import random

direction_table = [["x", 1], ["x", -1], ["y", 1], ["y", -1]]

random.seed(1)


class SnakeCore:
    def __init__(self, x=10, y=10, datatype=np.int16):
        self.datatype = datatype
        self.direction = None
        self.gameboard = None
        self.snake_body = []

        self.reset_gameboard(x, y)

    def reset_gameboard(self, x_in=None, y_in=None):
        # Use default values if not reassigned
        if x_in is None:
            x_in = self.gameboard.shape[0] - 2

        if y_in is None:
            y_in = self.gameboard.shape[1] - 2

        # Update variable
        self.gameboard = np.zeros((x_in + 2, y_in + 2), dtype=self.datatype)

        # Fill boundary with -2
        self.gameboard[:, 0] = -2
        self.gameboard[:, y_in + 1] = -2
        self.gameboard[0, :] = -2
        self.gameboard[x_in + 1, :] = -2

        # TODO: discuss design decision
        # Randomly spawn head within 1 blocks range of the edge
        x_head = random.randint(2, x_in - 1)
        y_head = random.randint(2, y_in - 1)
        self.gameboard[x_head][y_head] = 1
        self.snake_body.append([x_head, y_head])

        # TODO: discuss design decision
        # Randomly spawn first food (different from head position)
        x_food = random.randint(1, x_in)
        y_food = random.randint(1, y_in)
        while x_food == x_head and y_food == y_head:
            x_food = random.randint(1, x_in)
            y_food = random.randint(1, y_in)
        self.gameboard[x_food][y_food] = -1

        # Randomize initial direction
        self.direction = direction_table[random.randint(0, 3)]

    def snake_move(self, direction=None):
        # TODO: faser if self.direction be index of the direction table

        if direction is not None:
            # Check if legal move (cannot turn 180 deg)
            if direction[0] == self.direction[0] and direction[1] != self.direction[1]:
                # TODO: discuss design decision
                # Useless input, move in previous direction
                direction = self.direction
            else:
                self.direction = direction
        else:
            # Repeat previous move
            direction = self.direction

        head_position = self.snake_body[-1]

        if direction[0] == "x":
            head_next_position = [head_position[0] + direction[1], head_position[1]]
            object_on_next_position = self.gameboard[head_next_position[0]][head_next_position[1]]
        elif direction[0] == "y":
            head_next_position = [head_position[0], head_position[1] + direction[1]]
            object_on_next_position = self.gameboard[head_next_position[0]][head_next_position[1]]
        else:
            raise ValueError("wtf")

        # Collision check
        if object_on_next_position != 0:
            # Hit boundary or body
            if object_on_next_position == -2 or object_on_next_position > 0:
                return False
            elif object_on_next_position == -1:
                # Just append to body and no movement
                self.snake_body.append(head_next_position)
                # Remove food
                self.gameboard[head_next_position[0]][head_next_position[1]] += 1
                # Spawn new food
                if not self.spawn_food():
                    return False
                # Update gameboard
                for i in range(len(self.snake_body)):
                    self.gameboard[self.snake_body[i][0]][self.snake_body[i][1]] += 1
                return True
            else:
                raise ValueError("wtf")
        else:
            # Normal movement
            tail_previous_position = self.snake_body.pop(0)
            self.gameboard[tail_previous_position[0]][tail_previous_position[1]] = 0
            self.snake_body.append(head_next_position)
            # Update gameboard
            for i in range(len(self.snake_body)):
                self.gameboard[self.snake_body[i][0]][self.snake_body[i][1]] += 1
            return True

    def spawn_food(self):
        valid_position_list = []

        # TODO: faster if use table to keep track of available positions
        # Scan available positions and record
        for x in range(1, self.gameboard.shape[0] - 1):
            for y in range(1, self.gameboard.shape[1] - 1):
                if self.gameboard[x][y] == 0:
                    valid_position_list.append([x, y])

        if len(valid_position_list) == 0:
            return False
        else:
            i = random.randint(0, len(valid_position_list)-1)
            self.gameboard[valid_position_list[i][0]][valid_position_list[i][1]] = -1
            return True
