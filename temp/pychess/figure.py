import pygame
import os

black_figures = {
    "rook": 'figures\\Black\\rook.png',
    "knight": 'figures\\Black\\knight.png',
    "bishop": 'figures\\Black\\bishop.png',
    "king": 'figures\\Black\\king.png',
    "queen": 'figures\\Black\\queen.png',
    "pawn": 'figures\\Black\\pawn.png'
}

white_figures = {
    "rook": 'figures\\White\\rook.png',
    "knight": 'figures\\White\\knight.png',
    "bishop": 'figures\\White\\bishop.png',
    "king": 'figures\\White\\king.png',
    "queen": 'figures\\White\\queen.png',
    "pawn": 'figures\\White\\pawn.png'
}

def getFigureSprite(figureNum):
    if(figureNum == 1 or figureNum == 8): return pygame.image.load(os.path.join(os.getcwd(), black_figures["rook"]))
    if(figureNum == 2 or figureNum == 7): return pygame.image.load(os.path.join(os.getcwd(), black_figures["knight"]))
    if(figureNum == 3 or figureNum == 6): return pygame.image.load(os.path.join(os.getcwd(), black_figures["bishop"]))
    if(figureNum == 4): return pygame.image.load(os.path.join(os.getcwd(), black_figures["king"]))
    if(figureNum == 5): return pygame.image.load(os.path.join(os.getcwd(), black_figures["queen"]))
    if(figureNum >= 9 and figureNum <= 16): return pygame.image.load(os.path.join(os.getcwd(), black_figures["pawn"]))
    if(figureNum == 25 or figureNum == 32): return pygame.image.load(os.path.join(os.getcwd(), white_figures["rook"]))
    if(figureNum == 26 or figureNum == 31): return pygame.image.load(os.path.join(os.getcwd(), white_figures["knight"]))
    if(figureNum == 27 or figureNum == 30): return pygame.image.load(os.path.join(os.getcwd(), white_figures["bishop"]))
    if(figureNum == 28): return pygame.image.load(os.path.join(os.getcwd(), white_figures["king"]))
    if(figureNum == 29): return pygame.image.load(os.path.join(os.getcwd(), white_figures["queen"]))
    if(figureNum >= 17 and figureNum <= 24): return pygame.image.load(os.path.join(os.getcwd(), white_figures["pawn"]))

class Square(pygame.sprite.Sprite):
    def __init__(self, position, color, size):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

class Figure(pygame.sprite.Sprite):
    def __init__(self, position, figureType, chessboardPlacement):
        super().__init__()
        # if (figureType > 0):
        #     self.image = pygame.image.load(white_figures[figureType-1])
        # elif (figureType < 0):
        #     self.image = pygame.image.load(black_figures[abs(figureType+1)])
        self.chessboardPlacement = chessboardPlacement
        self.image = getFigureSprite(figureType)
        self.image = pygame.transform.smoothscale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

    def getPosition(self):
        return pygame.Vector2(self.rect.x, self.rect.y)

    def setPosition(self, pos=None):
        if type(pos) == pygame.Vector2:
            self.rect.x = pos.x
            self.rect.y = pos.y
        else:
            raise Exception('No arguments provided!')
        return