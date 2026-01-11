import pygame
from constants import SCREEN_HEIGHT, PIXELS_PER_METER

class Projectile:
    def __init__(self, initial_position, initial_velocity, initial_acceleration, radius):
        self.position = initial_position
        self.velocity = initial_velocity
        self.radius = radius
        self.acceleration = initial_acceleration

    def draw(self, screen):
        x, y = self.position
        x_pixel, y_pixel = x * PIXELS_PER_METER, y * PIXELS_PER_METER
        y_pixel = SCREEN_HEIGHT - y_pixel
        draw_position = (x_pixel, y_pixel)
        print(draw_position)
        pygame.draw.circle(screen, "white", draw_position, self.radius, 5)

    
    def update(self, dt):

        x, y = self.position
        vx, vy = self.velocity
        ax, ay = self.acceleration

        x += vx * dt
        y += vy * dt
        self.position = (x, y)

        vx += ax * dt
        vy += ay * dt
        self.velocity = (vx, vy)

    
