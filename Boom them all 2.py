from ftplib import all_errors

import pygame
import os
import sys

from random import randrange


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


class Bomb(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__()
        self.image = load_image("bomb.png")
        self.image_boom = load_image("boom.png")
        self.rect = self.image.get_rect()
        self.rect.x = randrange(width - self.rect.width)
        self.rect.y = randrange(height - self.rect.height)
        while pygame.sprite.spritecollideany(self, all_sprites):
            self.rect.x = randrange(width - self.rect.width)
            self.rect.y = randrange(height - self.rect.height)
        all_sprites.add(self)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos) and self.image != self.image_boom:
            self.image = self.image_boom
            self.rect.x -= 25
            self.rect.y -= 25


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Пример 1')
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)

    running = True
    screen.fill("black")

    all_sprites = pygame.sprite.Group()
    for _ in range(10):
        Bomb()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.update(event)
        screen.fill("black")
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()