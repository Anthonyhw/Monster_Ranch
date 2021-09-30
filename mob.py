import pygame
from random import randint

class Mob(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        spritesheet = pygame.image.load("data\\skeleton-red_eyes-SWEN.png")
        for i in range(3):
            for j in range(4):
                img = spritesheet.subsurface([i * 24, j * 32], [24, 32])
                self.sprites.append(img)

        self.atual = 4
        self.cont = 0

        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, [80, 80])
        self.rect = self.image.get_rect()
        self.rect.center = [randint(0, 864), randint(0, 864)]

    def update(self, player):

        self.cont += 0.5

        if self.cont < 4:
            self.atual = 0
        elif self.cont < 8:
            self.atual = 4
        elif self.cont < 12:
            self.atual = 8
        elif self.cont < 16:
            self.atual = 4
        elif self.cont > 16:
            self.cont = 0

        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, [80, 80])

        if player.rect.x + 32 > self.rect.x:
            self.rect.x = self.rect.x + 1
        else:
            self.rect.x = self.rect.x - 1

        if player.rect.y + 32 > self.rect.y:
            self.rect.y = self.rect.y + 1
        else:
            self.rect.y = self.rect.y - 1

        if self.rect.colliderect(player):
            return True
            #self.rect.x = randint(0, 864)
            #self.rect.y = randint(0, 816)