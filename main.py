import pygame
from sys import exit
from player import Player
from mob import Mob
from bullet import Bullet

pygame.init()
pygame.mixer.music.load("data\\Venus.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

class Overlap(pygame.sprite.Sprite):
    def __init__(self, *groups, img):
        super().__init__(*groups)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

def main():
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

    m1 = Mob()
    mobs.add(m1)
    fonte = pygame.font.SysFont("arial", 40, True, True)
    lose = fonte.render(f"You lose. Press RETURN to restart.", True, [255, 255, 255])
    score = 0

    fundo = pygame.image.load("data\\forest.png")

    shoot = pygame.mixer.Sound("data\\8bit_gunloop_explosion.wav")
    shoot.set_volume(0.2)

    ol = pygame.image.load("data\\overlap.png")

    timer = 0

    gameLoop = True


    def draw():
        display.fill([25, 25, 25])

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
                while True:
                    objectGroup.draw(display)
                    mobs.draw(display)
                    bullet_group.draw(display)
                    pygame.display.flip()
                    display.blit(lose, [100, 400])
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                main()
                        if event.type == pygame.QUIT:
                            exit()

            for bullet in bullet_group:
                for enemy in mobs:
                    if bullet.rect.colliderect(enemy.rect):
                        bullet.kill()
                        enemy.kill()
                        score += 1

            objectGroup.draw(display)
            mobs.draw(display)
            bullet_group.draw(display)
            print(pl.rect.top)

            bullet_group.update(pl)
            objectGroup.update()
            mobs.update(pl)
            display.blit(ol, [0, 0])
            pygame.display.flip()


main()
