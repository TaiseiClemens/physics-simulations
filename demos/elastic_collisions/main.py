import pygame
from disk import Disk
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PIXELS_PER_METER, TIME_MULTIPLIER

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    disks = [Disk((-2, 0.4), (1, 0), 5, 0.3), Disk((-2, -0.55), (1, 0), 5, 0.3), Disk((0, 0), (0, 0), 5, 0.3)]
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        # Updates
        for disk in disks:
            list_without_disk = [item for item in disks if item != disk]
            disk.update(dt, list_without_disk)
            disk.draw(screen, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

        pygame.display.flip()
        dt = clock.tick(120) / 1000 * TIME_MULTIPLIER 

if __name__ == "__main__":
    main()
