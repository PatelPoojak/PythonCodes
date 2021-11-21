import pygame
import numpy as np
import sys

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15

BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

RED = (255, 0, 0)
BG_COLOR = (255, 0, 0)
LINE_COLOR = (255, 165, 0)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

SQUARE_SIZE = 200

board = np.zeros((BOARD_ROWS, BOARD_COLS))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(BG_COLOR)
pygame.display.set_caption("TIC TAC TOE")

def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (SCREEN_WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (SCREEN_WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, SCREEN_HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, SCREEN_HEIGHT), LINE_WIDTH)

def available_square(row, col):
    is_available = False
    if board[row][col] == 0:
        is_available = True
    else:
        is_available = False
    return is_available


def mark_square(row, col, player):
    board[row][col] = player


def draw_vertical_winning_line(col, player):
    posX = col * SQUARE_SIZE + SQUARE_SIZE // 2

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (posX, 15), (posX, SCREEN_HEIGHT - 15), WIN_LINE_WIDTH)


def draw_horizontal_winning_line(row, player):
    posY = row * SQUARE_SIZE + SQUARE_SIZE // 2

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, posY), (SCREEN_WIDTH - 15, posY), WIN_LINE_WIDTH)


def draw_asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, SCREEN_HEIGHT - 15), (SCREEN_WIDTH - 15, 15), WIN_LINE_WIDTH)


def draw_desc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, 15), (SCREEN_WIDTH - 15, SCREEN_HEIGHT - 15), WIN_LINE_WIDTH)


def check_win(player):
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True

    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (
                int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS,
                                   CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 CROSS_WIDTH)


def restart():
	screen.fill( BG_COLOR )
	draw_lines()
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			board[row][col] = 0

player = 1
game_over = False

running = True
draw_lines()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y
            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)
            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                player = player % 2 + 1
                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                game_over = False

    pygame.display.update()
