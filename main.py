import pygame
from pygame.locals import *
from sys import exit
from player import Player

pygame.init()
alt = 1920
larg = 1020
clock = pygame.time.Clock()
display = pygame.display.set_mode([alt, larg])
pygame.display.set_caption("Monster Ranch")

objectGroup = pygame.sprite.Group()

player = Player(objectGroup)

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
        clock.tick(1000)
        mensagem = fonte.render(f"Score: {pontos}", True, [255, 255, 255])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shoot.play()
        draw()
        player.update()
        objectGroup.draw(display)
        display.blit(mensagem, [800, 20])
        pygame.display.update()
