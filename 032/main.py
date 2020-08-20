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
        figures.add(Figure((64*x, 64*y), FIGURE_NUMS[h]))
    if h % 8 == 7:
        x += 1
        y = 0
    else:
        y += 1
del x, y

dx, dy, n = 0, 0, 0
dragging, mouseClicked = False, False
mouseX, mouseY = 0, 0
mousePos = pygame.Vector2()

print(len(chessboard))
print(len(figures))

def toChessNote(p):
    pass

def toCoord(a, b):
    pass

def move():
    pass

def gameLoop():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)

        for i, figure in enumerate(figures, start=0):
            if FIGURE_NUMS[i] == 0: continue
            if event.type == MOUSEBUTTONDOWN or mouseClicked:
                mouseClicked = True
                if figure.rect.contains()
        
        if event.type == MOUSEMOTION:
            pass
        
        if event.type == MOUSEBUTTONUP:
            pass
    
    # for entity in all_sprites:
    #     displaysurface.blit(entity.surf, entity.rect)

    chessboard.draw(displaysurface)
    figures.draw(displaysurface)

    pygame.display.update()
    clear(displaysurface)

    FramePerSec.tick(FPS)

if __name__ == "__main__":
    while True:
        gameLoop()