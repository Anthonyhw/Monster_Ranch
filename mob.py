import pygame

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

        self.atual = 0
        self.cont = 0

        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)


    def update(self, player):

        self.cont += 1

        if self.cont < 4:
            self.atual = 4
        elif self.cont < 8:
            self.atual = 8
        elif self.cont < 12:
            self.atual = 0
        elif self.cont > 12:
            self.cont = 0


        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, [100, 100])

        if (player.rect.x > self.rect.x):
            self.rect.x = self.rect.x + 1
        else:
            self.rect.x = self.rect.x - 1



        if (player.rect.y > self.rect.y):
            self.rect.y = self.rect.y + 1
        else:
            self.rect.y = self.rect.y - 1