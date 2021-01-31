import math, random, sys
import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('airplane.png')
        self.rect = self.image.get_rect(center = (screen_width/2, 700))

pygame.init()
clock = pygame.time.Clock()
W, H = 1280, 720
HW, HH = W / 2, H / 2
DS = pygame.display.set_mode((W, H))
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

AREA = W * H
player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)
bg = pygame.image.load('photo800x800.jpeg').convert()
bgWidth, bgHeight = bg.get_rect().size

stageWidth = bgWidth * 2
stagePosX = 0

startScrollingPosX = HW

circleRadius = 25
circlePosX = circleRadius

playerPosX = circleRadius
playerPosY = 585
playerVelocityX = 0

while True:

    screen.blit(bg, (0, 0))
    keys = pygame.key.get_pressed()

    if keys[K_RIGHT]:
        playerVelocityX = 1
    elif keys[K_LEFT]:
        playerVelocityX = -1
    else:
        playerVelocityX = 0

    playerPosX += playerVelocityX
    if playerPosX > stageWidth - circleRadius: playerPosX = stageWidth - circleRadius
    if playerPosX < circleRadius: playerPosX = circleRadius
    if playerPosX < startScrollingPosX: circlePosX = playerPosX
    elif playerPosX > stageWidth - startScrollingPosX: circlePosX = playerPosX - stageWidth + W
    else:
            circlePosX = startScrollingPosX
            stagePosX += -playerVelocityX

    rel_x = stagePosX % bgWidth
    DS.blit(bg, (rel_x - bgWidth, 0))
    if rel_x < W:
        DS.blit(bg, (rel_x, 0))

    player_group.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    player_group.update()
    pygame.display.flip()
    pygame.display.update()
    clock.tick(100)
