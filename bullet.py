import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, flip):
        super().__init__()
        self.image = pygame.Surface([5, 5])
        self.image.fill([0, 0, 0])
        self.rect = self.image.get_rect(center=[x + 45, y + 45])
        self.flipped = flip

    def update(self, player):
        if self.flipped:
            self.rect.x += 15
            if self.rect.x > 864:
                self.kill()
        else:
            self.rect.x -= 15
            if self.rect.x < 0:
                self.kill()
