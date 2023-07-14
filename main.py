import pygame

import board_renderer
import game_logic
#import board_renderer

SIZE_X = 501
SIZE_Y = 501

pygame.init()
screen = pygame.display.set_mode((SIZE_X, SIZE_Y))
clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    board_renderer.draw_board(screen, SIZE_X, SIZE_Y)



    pygame.display.flip()

    clock.tick(60)

pygame.quit()
