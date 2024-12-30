import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Hero(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = load_image("creature.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, *args):
        if args:
            self.rect.x += args[0][0]
            self.rect.y += args[0][1]


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Герой двигается!')
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)

    running = True
    screen.fill("white")

    fps = 30
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    Hero(all_sprites)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            all_sprites.update((0, 1))
        if keys[pygame.K_UP]:
            all_sprites.update((0, -1))
        if keys[pygame.K_RIGHT]:
            all_sprites.update((1, 0))
        if keys[pygame.K_LEFT]:
            all_sprites.update((-1, 0))
        screen.fill("white")
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()