import pygame


class Hero(pygame.sprite.Sprite):
    def __init__(self, a, x, y):
        super().__init__(all_sprites)
        self.a = a
        self.image = pygame.Surface((a, a), pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, "blue", (0, 0, a, a))
        self.rect = pygame.Rect(x, y, a, a)
        self.vx = 0
        self.vy = 1

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if self.rect.y > height:
            self.kill()


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Платформы')
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)

    running = True
    screen.fill("black")

    all_sprites = pygame.sprite.Group()

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
        screen.fill("black")
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()

