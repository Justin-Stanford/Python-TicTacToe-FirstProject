import pygame
import gamelogic

SIZEX = 500
SIZEY = 500
rectWidth = SIZEX / 3
rectLength = SIZEY / 3

pygame.init()
screen = pygame.display.set_mode((SIZEX, SIZEY))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    for x in range(1,3): #each cell is going to be sizex / 3, sizey / 3
        for y in range(1,3):
            pygame.draw.line(screen,"white",((SIZEX / 3 * x), (SIZEY / 3 * y)))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
