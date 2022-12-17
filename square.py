# importation des librairies 
import pygame
from random import randint

# définition des constantes
BLACK = (33,33,33)
WHITE = (255,255,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 840
HEIGHT = 600

SQUARE_WIDTH = 50
SQUARE_HEIGHT = 50

RADIUS = 10

RACKET_HEIGHT = 100
RACKET_WIDTH = 10
RACKET_SPEED = 1


# définition de mon objet square
class Square(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.width = width
        self.color = color
        self.image = pygame.Surface([width, height])
        self.image.set_colorkey(BLACK)
        self.image.fill(BLACK)
        self.height = height

# je trace mon objet ball dans mon terrain de jeu
        pygame.draw.rect(self.image, self.color, [0,0, self.width, self.height])

        self.rect = self.image.get_rect()