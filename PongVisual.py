import pygame
from PongCore import PongCore

test_pongCore = PongCore()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pong")

WHITE = (255, 255, 255)

FPS = 60


def draw_window():
    WIN.fill(WHITE)

    offset_surface = pygame.Surface((840, 400))

    # Draw board A
    board_a_top = test_pongCore.board_A_position - test_pongCore.board_length / 2
    pygame.draw.rect(offset_surface, (255, 0, 0), pygame.Rect(0, board_a_top, 20, test_pongCore.board_length))

    # Draw board B
    board_a_top = test_pongCore.board_B_position - test_pongCore.board_length / 2
    pygame.draw.rect(offset_surface, (255, 0, 0), pygame.Rect(820, board_a_top, 20, test_pongCore.board_length))

    # Draw pong
    pygame.draw.rect(offset_surface, (255, 0, 0),
                     pygame.Rect(test_pongCore.pong_position[0] - 5 + 20, test_pongCore.pong_position[1] - 5, 10, 10))

    WIN.blit(offset_surface, (30, 50))

    pygame.display.update()


def pong_handel_movement(keys_pressed):
    if keys_pressed[pygame.K_q]:
        test_pongCore.move_board("A", -1)
    if keys_pressed[pygame.K_a]:
        test_pongCore.move_board("A", 1)
    if keys_pressed[pygame.K_w]:
        test_pongCore.move_board("B", -1)
    if keys_pressed[pygame.K_s]:
        test_pongCore.move_board("B", 1)
    if keys_pressed[pygame.K_SPACE]:
        test_pongCore.advance_pong()


def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        pong_handel_movement(keys_pressed)
        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
