import pygame
import sys
from pygame.locals import *
from constants import *
from figure import Figure, Square

def clear(surface): 
    surface.fill((0, 0, 0))

pygame.init()

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("chess lmao")

# figure = Figure((64, 64), -1)

chessboard = pygame.sprite.Group()
figures = pygame.sprite.Group()

x, y = 0, 0
clicked = False
pos = []
possibleMoves = []
oldPos = []
currPos = []
signal = False
clickedPiece = 0

for h in range(CHESSBOARD_TILES):
    currColor = None
    if (BOARD_NUMS[h] == 1):
        currColor = WHITE_COLOR
    else:
        currColor = BLACK_COLOR
    chessboard.add(Square((64*x, 64*y), currColor, (64, 64)))
    if h % 8 == 7:
        x += 1
        y = 0
    else:
        y += 1

x, y = 0, 0
for h in range(CHESSBOARD_TILES):
    if(FIGURE_NUMS[h] != 0):
        figures.add(Figure((64*x, 64*y), FIGURE_NUMS[h], h))
    if h % 8 == 7:
        y += 1
        x = 0
    else:
        x += 1
del x, y

print(len(chessboard))
print(len(figures))

# x coordinates increase from left to right, y coordinates increase from top to bottom

naHod = True

figureboard = [
    [ 22, 23, 24, 26, 25, 24, 23, 22],
    [ 21, 21, 21, 21, 21, 21, 21, 21],
    [ 0,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  0,  0,  0,  0,  0,  0,  0],
    [ 11, 11, 11, 11, 11, 11, 11, 11],
    [ 12, 13, 14, 16, 15, 14, 13, 12]
]

def drawSignal(x, y):
    pygame.draw.rect(displaysurface, (0, 139, 69), (y*64, x*64, 64, 64), 0)
    signal = True
    possibleMoves.append([x, y])


def rookMoves(x, y):
    x0 = x - 1
    y0 = y
    # move up
    while x0 >= 0:
        if figureboard[x0][y0] == 0:
            drawSignal(x0, y0)
        else:
            break
        x0 -= 1
    # move down
    x0 = x + 1
    while x0 < 8: 
        if figureboard[x0][y0] == 0:
            drawSignal(x0, y0)
        else:
            break
        x0 += 1
    # move right
    y0 = y + 1
    x0 = x
    while y0 < 8: 
        if figureboard[x0][y0] == 0:
            drawSignal(x0, y0)
        else:
            break
        y0 += 1
    # move left
    y0 = y - 1
    while y0 >= 0: 
        if figureboard[x0][y0] == 0:
            drawSignal(x0, y0)
        else:
            break
        y0 -= 1

def queenMoves(x, y):
    x0 = x - 1
    y0 = y
    # move up
    while x0 >= 0: 
        if figureboard[x0][y0] == 0:
            drawSignal(x0, y0)
        else:
            break
        x0 -= 1
    # move down
    x0 = x + 1
    while x0 < 8: 
        if figureboard[x0][y0] == 0:
            drawSignal(x0, y0)
        else:
            break
        x0 += 1
    # move right
    y0 = y + 1
    x0 = x
    while y0 < 8: 
        if figureboard[x0][y0] == 0:
            drawSignal(x0, y0)
        else:
            break
        y0 += 1
    # move left
    y0 = y - 1
    while y0 >= 0: 
        if figureboard[x0][y0] == 0:
            drawSignal(x0, y0)
        else:
            break
        y0 -= 1
    # move diagonally right up
    y0 = y + 1
    x0 = x - 1
    while y0 < 8 and x0 >= 0:
        if figureboard[x0][y0] == 0:
            drawSignal(x0, y0)
        else:
            break
        y0 += 1
        x0 -= 1

    # move diagonally left up
    y0 = y - 1
    x0 = x - 1
    while y0 >= 0 and x0 >= 0: 
        if figureboard[x0][y0] == 0:
            drawSignal(x0, y0)
        else:
            break
        y0 -= 1
        x0 -= 1

    # move diagonally right down
    y0 = y + 1
    x0 = x + 1
    while y0 < 8 and x0 < 8: 
        if figureboard[x0][y0] == 0:
            drawSignal(x0, y0)
        else:
            break
        y0 += 1
        x0 += 1

    # move diagonally left down
    y0 = y - 1
    x0 = x + 1
    while y0 >= 0 and x0 < 8: 
        if figureboard[x0][y0] == 0:
            drawSignal(x0, y0)
        else:
            break
        y0 -= 1
        x0 += 1

def bishopMoves(x, y):
    # move diagonally right up
    y0 = y + 1
    x0 = x - 1
    while y0 < 8 and x0 >= 0:
        if figureboard[x0][y0] == 0:
            drawSignal(x0, y0)
        else:
            break
        y0 += 1
        x0 -= 1    
        

    # move diagonally left up
    y0 = y - 1
    x0 = x - 1
    while y0 >= 0 and x0 >= 0: 
        if figureboard[x0][y0] == 0:
            drawSignal(x0, y0)
        else:
            break
        y0 -= 1
        x0 -= 1

    # move diagonally right down
    y0 = y + 1
    x0 = x + 1
    while y0 < 8 and x0 < 8: 
        if figureboard[x0][y0] == 0:
            drawSignal(x0, y0)
        else:
            break
        y0 += 1
        x0 += 1    

    # move diagonally left down
    y0 = y - 1
    x0 = x + 1
    while y0 >= 0 and x0 < 8: 
        if figureboard[x0][y0] == 0:
            drawSignal(x0, y0)
        else:
            break
        y0 -= 1
        x0 += 1    

def kingMoves(x, y):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if x + i >= 0 and x + i < 8 and y+j >= 0 and y + j < 8:
                if figureboard[x + i][y + j] == 0:
                    drawSignal(x + i, y + j)

def knightMoves(x, y):
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    for i in range(0, 8):
        if x + dx[i] >= 0 and x + dx[i] < 8 and y + dy[i] >= 0 and y + dy[i] < 8:
            if figureboard[x + dx[i]][y + dy[i]] == 0:
                drawSignal(x + dx[i], y + dy[i])

def pawnMoves(x, y, naHod):
    # When pawn moves diagonally
    if y + 1 < 8 and x - 1 >= 0:
        if figureboard[x - 1][y + 1] != 0 and figureboard[x - 1][y + 1]/10 == 2 and naHod:
            drawSignal(x - 1, y + 1)

    if y - 1 >= 0 and x - 1 >= 0:
        if figureboard[x - 1][y - 1] != 0 and figureboard[x - 1][y - 1]/10 == 2 and naHod:
            drawSignal(x - 1, y - 1)

    if y - 1 >= 0 and x + 1 < 8:
        if figureboard[x + 1][y - 1] != 0 and figureboard[x + 1][y - 1]/10 == 1 and naHod != True:
            drawSignal(x + 1, y - 1)

    if y + 1 < 8 and x + 1 < 8:
        if figureboard[x + 1][y + 1] != 0 and figureboard[x + 1][y + 1]/10 == 1 and naHod != True:
            drawSignal(x + 1, y + 1)

    # When pawn moves up
    if x == 6 and naHod:
        if figureboard[x - 1][y] == 0:
            if figureboard[x - 2][y] == 0:
                drawSignal(x - 1, y)
                drawSignal(x - 2, y)
            else:
                drawSignal(x - 1, y)
    elif figureboard[x - 1][y] == 0:
        drawSignal(x - 1, y)

    if x == 1 and naHod != True:
        if figureboard[x + 1][y] == 0:
            if figureboard[x + 2][y] == 0:
                drawSignal(x + 1, y)
                drawSignal(x + 2, y)
            else:
                drawSignal(x + 1, y)
    elif figureboard[x + 1][y] == 0:
        drawSignal(x + 1, y)



def showTheVariants(x, y):
    if figureboard[x][y] == 12 or figureboard[x][y] == 22:
        rookMoves(x, y)

    if figureboard[x][y] == 11 or figureboard[x][y] == 21:
        pawnMoves(x, y, naHod)

    if figureboard[x][y] == 13 or figureboard[x][y] == 23:
        knightMoves(x, y)

    if figureboard[x][y] == 14 or figureboard[x][y] == 24:
        bishopMoves(x, y)

    if figureboard[x][y] == 15 or figureboard[x][y] == 25:
        queenMoves(x, y)

    if figureboard[x][y] == 16 or figureboard[x][y] == 26:
        kingMoves(x, y)
    clickedPiece = FIGURE_NUMS[x][y]
    oldPos = [x, y]

def move():
    pass

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
        
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            clicked = True
            for i in possibleMoves:
                if (pos[0] >= i[0]*64 and pos[0] <= i[0]*64 + 64 and
                    pos[1] >= i[1]*64 and pos[1] <= i[1]*64 + 64):
                    FIGURE_NUMS[i[0]][i[1]] = clickedPiece
                    FIGURE_NUMS[oldPos[0]][oldPos[1]] = 0
                    currPos = [i[0], i[1]]

    
    # for entity in all_sprites:
    #     displaysurface.blit(entity.surf, entity.rect)

    chessboard.draw(displaysurface)

    if clicked == True:
        mcoord = [pos[1]//64, pos[0]//64]
        if figureboard[mcoord[0]][mcoord[1]] != 0:
            showTheVariants(mcoord[0], mcoord[1])

    # if signal == False:
    #    clicked = False

    figures.draw(displaysurface)
    pygame.display.update()
    clear(displaysurface)

    FramePerSec.tick(FPS)

