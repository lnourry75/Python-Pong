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


# création de mon objet raquette
class Racket(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.width = width
        self.color = color
        self.image = pygame.Surface([width, height])
        self.image.set_colorkey(BLACK)
        self.image.fill(BLACK)
        self.height = height

# ici je dessine ma raquette sur l'écran
        pygame.draw.rect(self.image, self.color, [0,0, self.width, self.height])

# je récupère ici mon objet avec de pouvoir le controler
        self.rect = self.image.get_rect()

# si le joueur se déplace vers le haut on diminue la valeur de y et on l'empeche de sortir de l'écran
    def Up(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0
    
    def Down(self, pixels):
        self.rect.y += pixels
        if self.rect.y > HEIGHT - self.height:
            self.rect.y = HEIGHT - self.height
