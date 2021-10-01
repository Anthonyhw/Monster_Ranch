import pygame
from sys import exit
from player import Player
from mob import Mob
from bullet import Bullet
from random import randint

pygame.init()
x = 864
y = 816
clock = pygame.time.Clock()
display = pygame.display.set_mode([x, y])
pygame.display.set_caption("Monster Ranch")

bullet_group = pygame.sprite.Group()

objectGroup = pygame.sprite.Group()
mobs = pygame.sprite.Group()

pl = Player()
objectGroup.add(pl)

collided = []

lista = list()
wave = 1
m1 = Mob()
mobs.add(m1)
respawn_x = 0
respawn_y = 0
fonte = pygame.font.SysFont("arial", 40, True, True)
score = 0

fundo = pygame.image.load("data\\forest.png")
pygame.mixer.music.load("data\\Venus.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

shoot = pygame.mixer.Sound("data\\8bit_gunloop_explosion.wav")
shoot.set_volume(0.2)


def draw():
    display.fill([25, 25, 25])

timer = 0

gameLoop = True
ispressing = False

if __name__ == '__main__':
    while gameLoop:
        clock.tick(60)
        mensagem = fonte.render(f"Score: {score}", True, [255, 255, 255])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if len(bullet_group) == 3:
                        pass
                    else:
                        bl = Bullet(pl.rect.x, pl.rect.y, pl.flip)
                        bl.add(bullet_group)
                        shoot.play()

        draw()
        display.blit(fundo, [0, 0])
        display.blit(mensagem, [350, 20])

        timer += 1

        if timer == 40:
            enemy = Mob()
            mobs.add(enemy)
            timer = 0





        collision = pygame.sprite.spritecollide(pl, mobs, False, pygame.sprite.collide_mask)

        if collision:
            for enemy in collision:
                respawn_x = -33
                respawn_y = -33
                while -32 < respawn_x < 896:
                    respawn_x = randint(-100, 896)
                while -60 < respawn_y < 900:
                    respawn_y = randint(-60, 900)

                enemy.rect.x = respawn_x
                enemy.rect.y = respawn_y

        for bullet in bullet_group:
            for enemy in mobs:
                if bullet.rect.colliderect(enemy.rect):
                    bullet.kill()
                    enemy.kill()
                    score += 1

        if score % 5 == 0:
            wave += 1

        objectGroup.draw(display)
        mobs.draw(display)
        bullet_group.draw(display)
        bullet_group.update(pl)
        objectGroup.update()
        mobs.update(pl)
        pygame.display.flip()
