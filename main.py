import pygame
import board_io
import game_logic

SIZE_X = 501
SIZE_Y = 501
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
turn = 1

pygame.init()
screen = pygame.display.set_mode((SIZE_X, SIZE_Y))
clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    board_io.draw_board(screen, board, SIZE_X, SIZE_Y)
    if(pygame.mouse.get_pressed(num_buttons=3)[0] == True):
        x_pos = pygame.mouse.get_pos()[0]
        y_pos = pygame.mouse.get_pos()[1]
        print(x_pos, y_pos)
        turn = board_io.mouse_click(board, turn, x_pos, y_pos, SIZE_X, SIZE_Y)
        print(turn)
    # for event in pygame.event.get():
    #     if event.type == pygame.MOUSEBUTTONDOWN:





    pygame.display.flip()

    clock.tick(60)

pygame.quit()
