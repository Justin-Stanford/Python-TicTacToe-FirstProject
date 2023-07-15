import pygame


def draw_board(screen, board, screen_size_x, screen_size_y):
    cell_width = screen_size_x / 3
    cell_height = screen_size_y / 3
    circle_x_offset = cell_width / 2
    circle_y_offset = cell_height / 2
    cross_tl_offset = (cell_width / 3, cell_width / 3)
    cross_tr_offset = ((cell_width / 3) * 2, cell_width / 3)
    cross_bl_offset = (cell_width / 3, (cell_width / 3) * 2)
    cross_br_offset = ((cell_width / 3) * 2, (cell_width / 3) * 2)

    line_width = int((screen_size_x + screen_size_y) / 300)

    for x in range(3):
        for y in range(3):
            start_coord = (screen_size_x / 3 * x, screen_size_y / 3 * y)
            rect = (start_coord, (cell_width, cell_height))
            circ_coord = (start_coord[0] + circle_x_offset, start_coord[1] + circle_y_offset)
            pygame.draw.rect(screen, "white", rect, line_width)
            if(board[x][y] == 1):
                pygame.draw.line(screen, "red", (start_coord[0] + cross_tl_offset[0], start_coord[1] + cross_tl_offset[1]), (start_coord[0] + cross_br_offset[0], start_coord[1] + cross_br_offset[1]), line_width * 3)
                pygame.draw.line(screen, "red", (start_coord[0] + cross_bl_offset[0], start_coord[1] + cross_bl_offset[1]), (start_coord[0] + cross_tr_offset[0], start_coord[1] + cross_tr_offset[1]), line_width * 3)
            elif(board[x][y] == 2):
                pygame.draw.circle(screen,"blue", circ_coord, (cell_height + cell_width) / 8)
                pygame.draw.circle(screen,"black", circ_coord, (cell_height + cell_width) / 9)

def mouse_click(board, turn, cursor_pos_x, cursor_pos_y, screen_size_x, screen_size_y):
    for x in range(3):
        for y in range(3):
            if(board[x][y] == 0):
                start_coord = (screen_size_x / 3 * x, screen_size_y / 3 * y)
                end_coord = ((screen_size_x / 3 * x) + (screen_size_x / 3), (screen_size_y / 3 * y) + (screen_size_y / 3))
                if(cursor_pos_x > start_coord[0] and cursor_pos_x < end_coord[0] and cursor_pos_y > start_coord[1] and cursor_pos_y < end_coord[1]):
                    board[x][y] = turn
                    if(turn == 1):
                        turn = 2
                    elif(turn == 2):
                        turn = 1
    return turn