import pygame, sys, os

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []

        # Outside of this tutorial, probably best to use a sprite sheet...
        directory = './frog'
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f):
                image = pygame.image.load(f)
                image = pygame.transform.scale(image, (384, 192))
                self.sprites.append(image)

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

pygame.init()
clock = pygame.time.Clock()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Sprite Animation')

moving_sprites = pygame.sprite.Group()
player = Player(10, 10)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    moving_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
