import pygame
from pygame.locals import *
from sys import exit
from player import Player
from mob import Mob

pygame.init()
alt = 1920
larg = 1020
clock = pygame.time.Clock()
display = pygame.display.set_mode([alt, larg])
pygame.display.set_caption("Monster Ranch")

objectGroup = pygame.sprite.Group()
mobs = pygame.sprite.Group()

pl = Player(objectGroup)

m1 = Mob(mobs)
m1.rect.x = 450
m1.rect.y = 450


fonte = pygame.font.SysFont("arial", 40, True, True)
pontos = 0


pygame.mixer.music.load("data\\Venus.wav")
pygame.mixer.music.play(-1)

shoot = pygame.mixer.Sound("data\\8bit_gunloop_explosion.wav")


def draw():
    display.fill([25, 25, 25])


gameLoop = True
ispressing = False

if __name__ == '__main__':
    while gameLoop:
        clock.tick(30)
        mensagem = fonte.render(f"Score: {pontos}", True, [255, 255, 255])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shoot.play()
        draw()
        pl.update()
        m1.update(pl)
        objectGroup.draw(display)
        mobs.draw(display)
        objectGroup.update()
        display.blit(mensagem, [800, 20])
        pygame.display.flip()
