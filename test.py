# importation des class objet via les autres fichiers python
from racket import Racket
from square import Square
from ball import Ball
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

# on initialise nos éléments dans pygame 
pygame.init()

# création d'une fenêtre de jeu nommé Pong
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# je créer chaque objet en appelant pour chacun sa classe particulière
RacketA = Racket(WHITE, RACKET_WIDTH, RACKET_HEIGHT)
RacketA.rect.x = 0
RacketA.rect.y = (HEIGHT - RACKET_HEIGHT) // 2

RacketB = Racket(WHITE, RACKET_WIDTH, RACKET_HEIGHT)
RacketB.rect.x = WIDTH - RACKET_WIDTH
RacketB.rect.y = (HEIGHT - RACKET_HEIGHT) // 2

ball = Ball(WHITE,2*RADIUS,2*RADIUS, RADIUS)
ball.rect.centerx = WIDTH // 2
ball.rect.centery = HEIGHT // 2

squareA = Square(RED, SQUARE_WIDTH, SQUARE_HEIGHT)
squareA.rect.x = 300
squareA.rect.y = 400

squareB = Square(GREEN, SQUARE_WIDTH, SQUARE_HEIGHT)
squareB.rect.x = 500
squareB.rect.y = 100

# je créer une variable qui contient tous les objets que je souhaite dessiner à l'écran
objects = pygame.sprite.OrderedUpdates()

# j'ajoute mes objets un par un dans cette variable
objects.add(RacketA)
objects.add(RacketB)
objects.add(ball)
objects.add(squareA)
objects.add(squareB)

Play = True
#  limiter les fps de l'écran pour pas que le jeu ne soit trop rapide
clock = pygame.time.Clock()

# j'initialise les score à 0
(scoreA, scoreB) = (0,0)

# tant que le jeu tourne on vérifie si l'utilisateur appuie sur le bouton quitter ou bien la touche echap pour quitter le jeu
while Play:
    clock.tick(400)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Play = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Play = False

# je définit les touches des 2 joueurs (haut/bas) et (s/w) qui bougeront à la valeur de la constante qur j'ai définit
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        RacketB.Up(RACKET_SPEED)
    if key[pygame.K_DOWN]:
        RacketB.Down(RACKET_SPEED)
    if key[pygame.K_w]:
        RacketA.Up(RACKET_SPEED)
    if key[pygame.K_s]:
        RacketA.Down(RACKET_SPEED)
    
# boucle pour éviter que la balle sorte de l'air de jeu et pour permette aux joueur de gagner des points
    ball.update()
    if ball.rect.centerx > (WIDTH - RADIUS):
        scoreA +=1
        ball.speed[0] *= -1
    if ball.rect.centerx < RADIUS:
        scoreB += 1
        ball.speed[0] *= -1
    if ball.rect.centery > (HEIGHT - RADIUS):
        ball.speed[1] *= -1
    if ball.rect.centery < RADIUS:
        ball.speed[1] *= -1

# si une des 2 raquettes touche la balle celle-ci est renvoyée
    if pygame.sprite.collide_mask(ball, RacketA) or pygame.sprite.collide_mask(ball, RacketB):
        ball.bounce()

# si la balle touche le carré rouge la balle est renvoyée vers le joueur
    if pygame.sprite.collide_mask(ball, squareA):
        (ball.rect.centerx, ball.rect.centery) = (WIDTH //2, HEIGHT//2)
        ball.bounce()
        
# si la balle touche le carré vert la balle est envoyée vers l'autre joueur
    if pygame.sprite.collide_mask(ball, squareB):
         (ball.rect.centerx, ball.rect.centery) = (WIDTH //2, HEIGHT//2)
         ball.attack()

# ici on met notre fond d'écran en noir et on trace la ligne du centre du terrain
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [WIDTH // 2, 0], [WIDTH // 2, HEIGHT], 5)

# je dessine tous mes objets sur l'écran
    objects.draw(screen)

# ici on affiche la score sous forme de  texte sur l'écran
    font = pygame.font.SysFont('arial', 50)
    score = font.render(str(scoreA), 1, WHITE)
    screen.blit(score, [WIDTH // 4, 10])
    score = font.render(str(scoreB), 1, WHITE)
    screen.blit(score, [3*WIDTH // 4, 10])

# mise à jour de l'écran
    pygame.display.flip()    

pygame.quit()

