import pygame
import sys
import random
bs = 4
s = 100
r = 10
ch = s * bs + r* (bs + 1)
background = (187, 173, 160)
colors = {
    0: (205, 195, 180),
    2: (240, 230, 220),
    4: (240, 230, 200),
    8: (240, 180, 120),
    16: (245, 150, 100),
    32: (245, 125, 95),
    64: (245, 95, 60),
    128: (235, 210, 115),
    256: (235, 205, 100),
    512: (235, 200, 80),
    1024: (235, 200, 65),
    2048: (235, 195, 45),
}
def hehe():
    pygame.init()
    screen = pygame.display.set_mode((ch, ch))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 48)
    board = []
    for i in range(bs):
        row = []
        for j in range(bs):
            row.append(0)
        board.append(row)
    heheha(board)
    heheha(board)
    running = True
    while running:
        screen.fill(background)
        draw_board(screen, board, font)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move_up(board)
                    heheha(board)
                elif event.key == pygame.K_DOWN:
                    move_down(board)
                    heheha(board)
                elif event.key == pygame.K_LEFT:
                    move_left(board)
                    heheha(board)
                elif event.key == pygame.K_RIGHT:
                    move_right(board)
                    heheha(board)
        if gameover(board):
            print("Game Over!")
            running = False
        clock.tick(30)

    pygame.quit()
def heheha(board):
    morb = []
    for i in range(bs):
        for j in range(bs):
            if board[i][j] == 0:
                morb.append((i, j))
    if morb:
        ran = random.choice(morb)
        i, j = ran
        board[i][j] = random.choices([2, 4], weights=[0.9, 0.1])[0]

def move_up(board):
    for j in range(bs):
        for i in range(1, bs):
            if board[i][j] != 0:
                for k in range(i, 0, -1):
                    if board[k - 1][j] == 0:
                        board[k - 1][j], board[k][j] = board[k][j], board[k - 1][j]
                    elif board[k - 1][j] == board[k][j]:
                        board[k - 1][j] *= 2
                        board[k][j] = 0
                        break
def move_down(board):
    for j in range(bs):
        for i in range(bs - 2, -1, -1):
            if board[i][j] != 0:
                for k in range(i, bs - 1):
                    if board[k + 1][j] == 0:
                        board[k + 1][j], board[k][j] = board[k][j], board[k + 1][j]
                    elif board[k + 1][j] == board[k][j]:
                        board[k + 1][j] *= 2
                        board[k][j] = 0
                        break
def move_left(board):
    for i in range(bs):
        for j in range(1, bs):
            if board[i][j] != 0:
                for k in range(j, 0, -1):
                    if board[i][k - 1] == 0:
                        board[i][k - 1], board[i][k] = board[i][k], board[i][k - 1]
                    elif board[i][k - 1] == board[i][k]:
                        board[i][k - 1] *= 2
                        board[i][k] = 0
                        break
def move_right(board):
    for i in range(bs):
        for j in range(bs - 2, -1, -1):
            if board[i][j] != 0:
                for k in range(j, bs - 1):
                    if board[i][k + 1] == 0:
                        board[i][k + 1], board[i][k] = board[i][k], board[i][k + 1]
                    elif board[i][k + 1] == board[i][k]:
                        board[i][k + 1] *= 2
                        board[i][k] = 0
                        break
def gameover(board):
    for i in range(bs):
        for j in range(bs):
            if board[i][j] == 0:
                return False
            if j < bs - 1 and board[i][j] == board[i][j + 1]:
                return False
            if i < bs - 1 and board[i][j] == board[i + 1][j]:
                return False
    return True
def draw_board(screen, board, font):
    for i in range(bs):
        for j in range(bs):
            pygame.draw.rect(screen, colors[board[i][j]], (r + j * (s + r), r + i * (s + r), s, s))
            if board[i][j] != 0:
                text = font.render(str(board[i][j]), True, (0, 0, 0))
                text_rect = text.get_rect(center=(r + j * (s + r) + s // 2, r + i * (s + r) + s // 2))
                screen.blit(text, text_rect)
            
hehe()
