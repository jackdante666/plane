import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('airplane.png')
        self.rect = self.image.get_rect(center = (screen_width/2, 700))

pygame.init()
clock = pygame.time.Clock()
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
bg = pygame.image.load('photo800x800.jpeg')
player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        player.rect.x += 5
    if keys[pygame.K_LEFT]:
        player.rect.x -= 5
    if keys[pygame.K_UP]:
        player.rect.y -= 5
    if keys[pygame.K_DOWN]:
        player.rect.y += 5

    pygame.display.update()
    screen.blit(bg, (0, 0))
    player_group.update()
    player_group.draw(bg)
    pygame.display.flip()
    clock.tick(30)