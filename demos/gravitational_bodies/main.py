import pygame
from planet import Planet
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PIXELS_PER_METER, TIME_MULTIPLIER

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    moon = Planet((0, 3.844e8), (1022, 0), 7.342e22, 5)
    earth = Planet((0, 0,), (0, 0), 5.972e24, 10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        # Updates
        moon.update(dt, [earth])
        earth.update(dt, [moon])

        moon.draw(screen, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        earth.draw(screen, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

        pygame.display.flip()
        dt = clock.tick(60) / 1000 * TIME_MULTIPLIER 

if __name__ == "__main__":
    main()
