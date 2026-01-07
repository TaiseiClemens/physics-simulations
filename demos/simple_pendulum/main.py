import pygame
import numpy as np
from pendulum import Pendulum
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PIXELS_PER_METER, TIME_MULTIPLIER

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    pendulum = Pendulum((4, 3), 2, np.pi/4, 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        # Updates
        pendulum.update(dt)
        pendulum.draw(screen, (0, 0))

        pygame.display.flip()
        dt = clock.tick(60) / 1000 * TIME_MULTIPLIER 

if __name__ == "__main__":
    main()
