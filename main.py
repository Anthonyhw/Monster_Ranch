import pygame
from pygame.locals import *
from sys import exit
from player import Player
from mob import Mob

pygame.init()
alt = 864
larg = 816
clock = pygame.time.Clock()
display = pygame.display.set_mode([alt, larg])
pygame.display.set_caption("Monster Ranch")

objectGroup = pygame.sprite.Group()
mobs = pygame.sprite.Group()

pl = Player(objectGroup)

m1 = Mob(mobs)



fonte = pygame.font.SysFont("arial", 40, True, True)
pontos = 0

fundo = pygame.image.load("data\\forest.png")
pygame.mixer.music.load("data\\Venus.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

shoot = pygame.mixer.Sound("data\\8bit_gunloop_explosion.wav")
shoot.set_volume(0.2)

def draw():
    display.fill([25, 25, 25])


gameLoop = True
ispressing = False

if __name__ == '__main__':
    while gameLoop:
        clock.tick(60)
        mensagem = fonte.render(f"Score: {pontos}", True, [255, 255, 255])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shoot.play()
        draw()
        display.blit(fundo, [0, 0])
        display.blit(mensagem, [350, 20])
        pl.update()
        lost = m1.update(pl)

        if lost == True:
            exit()
        objectGroup.draw(display)
        mobs.draw(display)
        objectGroup.update()
        pygame.display.flip()
