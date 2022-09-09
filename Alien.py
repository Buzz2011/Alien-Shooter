# Importing Modules
import pygame
import random

# Initialize
pygame.init()

clock = pygame.time.Clock()

# Screen
screen = pygame.display.set_mode((800, 600))

# background for game
bg = pygame.image.load('bgg.jpg')

# Caption And Icon
pygame.display.set_caption('Alien Shooter')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player and Alien
playerimg = pygame.image.load('rocket.png')
px = 370
py = 500
x_change = 0

alienimg = pygame.image.load('alien.png')
ax = random.randint(0, 800)
ay = 50
ax_change = 0
ay_change = 0


def player(px, py):
    screen.blit(playerimg, (px, py))


def alien(ax, ay):
    screen.blit(alienimg, (ax, ay))


# Main Loop
run = True
while run:

    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # PLayer Movements
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_change = -0.3
            if event.key == pygame.K_d:
                x_change = 0.3
            if event.key == pygame.K_LEFT:
                x_change = -0.3
            if event.key == pygame.K_RIGHT:
                x_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                x_change = 0

    if px <= 0:
        px = 0
    elif px >= 736:
        px = 736

        # Alien Movements
    if run == True:
        ay_change = 0.06

    ax += ax_change
    ay += ay_change

    px += x_change
    player(px, py)
    alien(ax, ay)
    pygame.display.update()
