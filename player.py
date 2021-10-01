import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("data\\perso_16x16.png").convert_alpha())
        self.sprites.append(pygame.image.load("data\\perso_16x16_2.png").convert_alpha())
        self.sprites.append(pygame.image.load("data\\walking1.png").convert_alpha())
        self.sprites.append(pygame.image.load("data\\walking2.png").convert_alpha())
        self.atual = 0
        self.cont = 0
        self.scale = 80
        self.flip = False

        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, [self.scale, self.scale])
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = [432, 408]

    def move(self):

        keys = pygame.key.get_pressed()

        self.cont += 0.05
        if self.cont < 2:
            self.atual = 2
        elif self.cont < 3:
            self.atual = 3
        elif self.cont > 3:
            self.cont = 1

        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, [self.scale, self.scale])

        if self.flip:
            self.image = pygame.transform.flip(self.image, True, False)

        if keys[pygame.K_d]:
            if self.rect.x >= 814:
                pass
            else:
                self.rect.x += 3
                self.flip = True

        if keys[pygame.K_a]:
            if self.rect.x <= -32:
                pass
            else:
                self.rect.x -= 3
                self.flip = False

        if keys[pygame.K_w]:
            self.rect.y -= 3

        if keys[pygame.K_s]:
            self.rect.y += 3

        """
        if keys[pygame.KEYUP]:
            self.atual = 0
            self.image = self.sprites[int(self.atual)]
        """

    def update(self, ):
        self.move()

