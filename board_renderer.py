import pygame


def draw_board(screen, size_x, size_y):
    cell_width = size_x / 3
    cell_height = size_y / 3
    line_width = int((size_x + size_y) / 300)

    for x in range(3):
        for y in range(3):
            rect = ((size_x / 3 * x, size_y / 3 * y), (cell_width, cell_height))
            pygame.draw.rect(screen, "white", rect, line_width)

# def draw_pieces(screen, board, SIZE_X, SIZE_Y):
#     line_width = int((SIZE_X + SIZE_Y) / 300)
#     for x in range(3):
#         for y in range(3)


def player_selection(coords, size_x, size_y):
    for x in range(3):
        for y in range(3):
            tl = [0 ]