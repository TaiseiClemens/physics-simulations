import pygame
from projectile import Projectile
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PIXELS_PER_METER

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    projectile = Projectile((0, 0), (5, 10), (0, -9.81), 5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        # Updates
        projectile.update(dt)
        projectile.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
