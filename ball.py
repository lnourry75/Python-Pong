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


# définition de mon objet ball
class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height, radius):
        super().__init__()
        self.radius = radius
        self.height = height
        self.color = color
        self.width = width
        self.speed = [1, 1]
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

    # je trace mon objet ball dans mon terrain de jeu
        pygame.draw.circle(self.image, color, (self.width // 2, self.height // 2), self.radius)
        self.rect = self.image.get_rect()

    # fonction qui permet a la balle de se déplacer 
    def update(self):
        self.rect.centerx += self.speed[0]
        self.rect.centery += self.speed[1]

    # fonction qui permet à la balle de rebondir avec une vitesse aléatoire
    def bounce(self):
        self.speed[0] *= -1
        self.speed[1] = randint(-2,2)

    # fonction qui me permet à la balle d'être renvoyée vers l'adversaire avec une vitesse aléatoire
    def attack(self):
        self.speed[0] *= 1
        self.speed[1] = randint(-2,2)