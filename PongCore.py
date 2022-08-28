import random
from math import sin, cos, pi

random.seed(1)


# TODO: check pong stuck at the very edge

class PongCore:
    def __init__(self,
                 l_x=800, l_y=400,
                 board_length=100, board_speed=400, board_reflex_angle=120,
                 pong_max_velocity=300, init_angle_range=60,
                 tick_rate=60
                 ):
        self.L_x = l_x
        self.L_y = l_y

        self.board_length = board_length
        self.board_speed = board_speed
        self.board_reflex_angle = board_reflex_angle

        self.pong_max_velocity = pong_max_velocity

        self.tick_rate = tick_rate

        # TODO: discuss if need to launch pong at random player
        init_angle = random.uniform((180 - init_angle_range) / 2, (180 + init_angle_range) / 2)
        self.pong_position = [l_x / 2, l_y / 2]
        self.pong_velocity = [pong_max_velocity * sin(init_angle / 180 * pi) * ((-1) ** random.randint(0, 1)),
                              pong_max_velocity * cos(init_angle / 180 * pi)]

        self.board_A_position = l_y / 2
        self.board_B_position = l_y / 2

    def advance_pong(self, need_collision_check=True):
        self.pong_position[0] += self.pong_velocity[0] / self.tick_rate
        self.pong_position[1] += self.pong_velocity[1] / self.tick_rate
        if need_collision_check:
            return self.collision_check()

    def collision_check(self):
        if self.pong_position[1] < 0 or self.pong_position[1] > self.L_y:
            # Invert y velocity
            self.pong_velocity[1] *= -1

        # hitting board A side
        if self.pong_position[0] < 0:
            # if hit board
            if self.board_A_position - self.board_length / 2 < self.pong_position[1] or \
                    self.board_A_position + self.board_length / 2 > self.pong_position[1]:
                # Reflect
                pa = self.pong_position[1] - (self.board_A_position - self.board_length / 2)
                p = (1 - pa / self.board_length) * self.board_reflex_angle + (180 - self.board_reflex_angle) / 2
                self.pong_velocity = [self.pong_max_velocity * sin(p / 180 * pi),
                                      self.pong_max_velocity * cos(p / 180 * pi)]
            else:
                # Game Over
                return False

        # hitting board B side
        if self.pong_position[0] > self.L_x:
            # if hit board
            if self.board_B_position - self.board_length / 2 < self.pong_position[1] or \
                    self.board_B_position + self.board_length / 2 > self.pong_position[1]:
                # Reflect
                pa = self.pong_position[1] - (self.board_B_position - self.board_length / 2)
                p = (1 - pa / self.board_length) * self.board_reflex_angle + (180 - self.board_reflex_angle) / 2
                self.pong_velocity = [-1 * self.pong_max_velocity * sin(p / 180 * pi),
                                      self.pong_max_velocity * cos(p / 180 * pi)]
            else:
                # Game Over
                return False

        return True

    def move_board(self, board_id, direction=0):
        # TODO: reduce duplicate logic
        if board_id == "A":
            if direction == 1:
                # Check if hits edge
                if self.board_A_position + self.board_length/2 < self.L_y:
                    self.board_A_position += self.board_speed / self.tick_rate
                    return True
                else:
                    return False
            elif direction == -1:
                # Check if hits edge
                if self.board_A_position - self.board_length/2 > 0:
                    self.board_A_position -= self.board_speed / self.tick_rate
                    return True
                else:
                    return False
            else:
                return False

        elif board_id == "B":
            if direction == 1:
                # Check if hits edge
                if self.board_B_position + self.board_length/2 < self.L_y:
                    self.board_B_position += self.board_speed / self.tick_rate
                    return True
                else:
                    return False
            elif direction == -1:
                # Check if hits edge
                if self.board_B_position - self.board_length/2 > 0:
                    self.board_B_position -= self.board_speed / self.tick_rate
                    return True
                else:
                    return False
            else:
                return False

        else:
            return False
