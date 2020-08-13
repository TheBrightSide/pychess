import pygame
import sys
from pygame.math import *
from pygame import mouse
from pygame.locals import *
from constants import *
from figure import Figure, Square

def clear(surface): 
    surface.fill((0, 0, 0))

pygame.init()

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("chess lmao")

chessboard = pygame.sprite.Group()
figures = pygame.sprite.Group()

x, y, = 0, 0
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

x, y, = 0, 0
for h in range(CHESSBOARD_TILES):
    if(FIGURE_NUMS[h] != 0):
        figures.add(Figure((64*x, 64*y), FIGURE_NUMS[h], h))
    if h % 8 == 7:
        x += 1
        y = 0
    else:
        y += 1
del x, y

selectedFigure = -1
selected = False
mousePosition = Vector2()

def toChessNote(p):
    s = ""
    s += chr(int(p.x) // CHESSBOARD_TILES + 97)
    s += chr(7-int(p.y) // CHESSBOARD_TILES + 49)
    return s

def toCoord(chessCoord):
    x = ord(chessCoord[0]) - 97
    y = 7 - ord(chessCoord[0]) + 49
    return Vector2(x * CHESSBOARD_TILES, y * CHESSBOARD_TILES)

# def move(strg):
#     oldPos = toCoord(strg[0], strg[1])
#     newPos = toCoord(strg[2], strg[3])

#     for figure in figures:
#         if FIGURE_NUMS[figure.chessboardPlacement] == 0: continue
#         if figure.getPosition() == newPos: figure.setPosition(Vector2(-100, -100))
    
#     for figure in figures:
#         if FIGURE_NUMS[figure.chessboardPlacement] == 0: continue
#         if figure.getPosition() == oldPos: figure.setPosition(newPos)

#     if (strg=="e1g1"):
#         if (position.find("e1")==-1):
#             move("h1f1")
# 	if (strg=="e8g8"):
#         if (position.find("e8")==-1):
#             move("h8f8")
# 	if (strg=="e1c1"):
#         if (position.find("e1")==-1):
#             move("a1d1")
# 	if (strg=="e8c8"):
#         if (position.find("e8")==-1):
#             move("a8d8")

while True:
    mousePosition = Vector2(mouse.get_pos())

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)

        for i, figure in enumerate(figures, start=0):
            if FIGURE_NUMS[i] == 0: continue
            if event.type == MOUSEBUTTONDOWN:
                if figure.rect.contains(pygame.Rect(int(mousePosition.x), int(mousePosition.y), 1, 1)) and not selected:
                    selectedFigure = i
                    selected = True
                elif selected and selectedFigure == i:
                    print(toChessNote(figure.rect))
                    selectedFigure = -1
                    selected = False
        
        # if event.type == MOUSEBUTTONUP:
        #     p = figures.sprites()[selectedFigure].getPosition()
        #     # newPos = Vector2(CHESSBOARD_TILES * p.x / CHESSBOARD_TILES, CHESSBOARD_TILES * p.y / CHESSBOARD_TILES)
        #     newPos = toCoord(toChessNote(Vector2(p.x, p.y)))
        #     # strg = toChessNote(oldPos) + toChessNote(newPos)
        #     # move(strg)
        #     figures.sprites()[selectedFigure].setPosition(newPos)

        #     print(strg)

    clear(displaysurface)

    chessboard.draw(displaysurface)
    figures.draw(displaysurface)

    pygame.display.update()
    FramePerSec.tick(FPS)