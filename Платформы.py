import pygame


class Hero(pygame.sprite.Sprite):
    def __init__(self, a, x, y):
        super().__init__(all_sprites)
        self.a = a
        self.image = pygame.Surface((a, a), pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, "blue", (0, 0, a, a))
        self.rect = pygame.Rect(x, y, a, a)

        self.vy = 1

    def update(self):
        if not pygame.sprite.spritecollideany(self, horizontal_wall):
            self.rect = self.rect.move(0, self.vy)
            if self.rect.y > height:
                self.kill()

    def move_horizontal(self, x):
        self.rect = self.rect.move(x, 0)


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(horizontal_wall)
        self.image = pygame.Surface((50, 10), pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, "gray", (0, 0, 50, 10))
        self.rect = pygame.Rect(x, y, 50, 10)


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Платформы')
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)

    running = True
    screen.fill("black")

    all_sprites = pygame.sprite.Group()
    horizontal_wall = pygame.sprite.Group()

    fps = 50
    clock = pygame.time.Clock()

    hero = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    if not hero:
                        hero = Hero(20, *event.pos)
                    else:
                        hero.kill()
                        hero = Hero(20, *event.pos)
                if event.button == 1:
                    Platform(*event.pos)
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_LEFT]:
                    hero.move_horizontal(-10)
                if pygame.key.get_pressed()[pygame.K_RIGHT]:
                    hero.move_horizontal(10)
        screen.fill("black")
        all_sprites.update()
        all_sprites.draw(screen)
        horizontal_wall.draw(screen)
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
