import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data\perso_16x16.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(0, 0, 100, 100)


    def update(self, *args):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += 1
            self.image = pygame.image.load("data\walking1.png")
            self.image = pygame.transform.scale(self.image, [100, 100])
            self.image = pygame.image.load("data\walking2.png")
            self.image = pygame.transform.scale(self.image, [100, 100])
        elif keys[pygame.K_a]:
            self.rect.x -= 1
        elif keys[pygame.K_w]:
            self.rect.y -= 1
        elif keys[pygame.K_s]:
            self.rect.y += 1
        elif keys[pygame.K_w] and keys[pygame.K_d]:
            self.rect.y -= 1
            self.rect.x += 1
        elif keys[pygame.K_w] and keys[pygame.K_a]:
            self.rect.y -= 1
            self.rect.x -= 1
        elif keys[pygame.K_s] and keys[pygame.K_a]:
            self.rect.y += 1
            self.rect.x += 1
        elif keys[pygame.K_s] and keys[pygame.K_a]:
            self.rect.y += 1
            self.rect.x -= 1