import pygame
from random import randint


class Mob(pygame.sprite.Sprite):
    def __init__(self):

        respawn_x = randint(-40, 904)
        respawn_y = randint(-40, 856)

        aleat = randint(1, 2)

        if aleat == 1:
            respawn_x = randint(-80, 904)
            while respawn_y > 0 and respawn_y < 816:
                respawn_y = randint(-80, 856)
        elif aleat == 2:
            while respawn_x > 0 and respawn_x < 864:
                respawn_x = randint(-80, 904)
            respawn_y = randint(-80, 856)



        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        sprite_sheet = pygame.image.load("data\\skeleton-red_eyes-SWEN.png")
        for i in range(3):
            for j in range(4):
                img = sprite_sheet.subsurface([i * 24, j * 32], [24, 32])
                img = pygame.transform.scale(img, [80, 80])
                self.sprites.append(img)

        self.atual = 4
        self.cont = 0

        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = [respawn_x, respawn_y]

    def move(self, player):
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

        if player.rect.x > self.rect.x:
            self.rect.x = self.rect.x + 1
        else:
            self.rect.x = self.rect.x - 1

        if player.rect.y > self.rect.y:
            self.rect.y = self.rect.y + 1
        else:
            self.rect.y = self.rect.y - 1

    def update(self, player):
        self.move(player)
