import pygame
import os
from SnakeCore import SnakeCore

test_snakeCore = SnakeCore()

WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("tanchishe")

WHITE = (255, 255, 255)

SIZE = 60
FPS = 2
VEL = 5

APPLE_IMAGE = pygame.image.load(os.path.join('asset', 'apple.png'))
APPLE_IMAGE_SCALE = pygame.transform.scale(APPLE_IMAGE, (SIZE, SIZE))

BRICK_IMAGE = pygame.image.load(os.path.join('asset', 'brick.png'))
BRICK_IMAGE_SCALE = pygame.transform.scale(BRICK_IMAGE, (SIZE, SIZE))

HEAD_IMAGE = pygame.image.load(os.path.join('asset', 'head.png'))
HEAD_IMAGE_SCALE = pygame.transform.scale(HEAD_IMAGE, (SIZE, SIZE))

BODY_IMAGE = pygame.image.load(os.path.join('asset', 'body.png'))
BODY_IMAGE_SCALE = pygame.transform.scale(BODY_IMAGE, (SIZE, SIZE))


def draw_window(apple):
    WIN.fill(WHITE)
    for i in range(12):
        for j in range(12):
            if test_snakeCore.gameboard[i][j] == -2:
                WIN.blit(BRICK_IMAGE_SCALE, (i*SIZE, j*SIZE))

            if test_snakeCore.gameboard[i][j] == -1:
                WIN.blit(APPLE_IMAGE_SCALE, (i*SIZE, j*SIZE))

            if test_snakeCore.gameboard[i][j] == 1:
                WIN.blit(HEAD_IMAGE_SCALE, (i*SIZE, j*SIZE))

            if test_snakeCore.gameboard[i][j] > 1:
                WIN.blit(BODY_IMAGE_SCALE, (i * SIZE, j * SIZE))

    pygame.display.update()


def snake_handel_movement(keys_pressed, apple):
    if keys_pressed[pygame.K_a]:
        test_snakeCore.snake_move(["x", -1])
    if keys_pressed[pygame.K_w]:
        test_snakeCore.snake_move(["y", -1])
    if keys_pressed[pygame.K_d]:
        test_snakeCore.snake_move(["x", 1])
    if keys_pressed[pygame.K_s]:
        test_snakeCore.snake_move(["y", 1])


def main():
    apple = pygame.Rect(250, 250, SIZE, SIZE)

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        snake_handel_movement(keys_pressed, apple)
        draw_window(apple)

    pygame.quit()


if __name__ == "__main__":
    main()
