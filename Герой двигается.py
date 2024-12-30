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
            if args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_UP:
                self.rect.y -= 10
            if args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_DOWN:
                self.rect.y += 10
            if args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_RIGHT:
                self.rect.x += 10
            if args[0].type == pygame.KEYDOWN and args[0].key == pygame.K_LEFT:
                self.rect.x -= 10


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Герой двигается!')
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)

    running = True
    screen.fill("white")

    all_sprites = pygame.sprite.Group()
    Hero(all_sprites)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                all_sprites.update(event)
        screen.fill("white")
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()