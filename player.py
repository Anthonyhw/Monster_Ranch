import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("data/perso_16x16.png"))
        self.sprites.append(pygame.image.load("data/walking1.png"))
        self.sprites.append(pygame.image.load("data/walking2.png"))
        self.atual = 0
        self.cont = 1

        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, [200, 200])
        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100


    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += 10
            self.cont += 0.01
            if self.cont < 2:
                self.atual = 1
            elif self.cont < 3:
                self.atual = 2
            elif self.cont > 3:
                self.cont = 1

            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, [200, 200])
        elif keys[pygame.K_a]:
            self.rect.x -= 10
            self.cont += 0.01
            print(self.cont)
            if self.cont < 2:
                self.atual = 1
            elif self.cont < 3:
                self.atual = 2
            elif self.cont > 3:
                self.cont = 1

            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, [200, 200])
        elif keys[pygame.K_w]:
            self.rect.y -= 10
            self.cont += 0.01
            print(self.cont)
            if self.cont < 2:
                self.atual = 1
            elif self.cont < 3:
                self.atual = 2
            elif self.cont > 3:
                self.cont = 1

            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, [200, 200])
        elif keys[pygame.K_s]:
            self.rect.y += 10
            self.cont += 0.01
            print(self.cont)
            if self.cont < 2:
                self.atual = 1
            elif self.cont < 3:
                self.atual = 2
            elif self.cont > 3:
                self.cont = 1

            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, [200, 200])

        if keys[pygame.KEYUP]:
            self.atual = 0
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, [200, 200])