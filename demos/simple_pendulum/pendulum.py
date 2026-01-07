import pygame
import numpy as np
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PIXELS_PER_METER, GRAVITY

class Pendulum:
    def __init__(self, pivot_position, length, initial_theta, initial_angular_velocity=0):
        self.pivot_position = pivot_position
        self.length = length
        self.theta = initial_theta
        self.angular_velocity = initial_angular_velocity
        self.angular_acceleration = 0
        self.bob_radius = 10
        self.update_position()

    def update_position(self):
        pivot_x, pivot_y = self.pivot_position
        self.position = (
            pivot_x + self.length * np.sin(self.theta),
            pivot_y - self.length * np.cos(self.theta)
        )

    def update(self, dt):
        self.angular_acceleration = (GRAVITY / self.length) * np.sin(self.theta)
        self.angular_velocity += self.angular_acceleration * dt
        self.theta += self.angular_velocity * dt
        self.update_position()

    def draw(self, screen, offset):
        x_offset, y_offset = offset

        pivot_x = self.pivot_position[0] * PIXELS_PER_METER + x_offset
        pivot_y = SCREEN_HEIGHT - (self.pivot_position[1] * PIXELS_PER_METER + y_offset)
        pivot_pixel = (int(pivot_x), int(pivot_y))

        bob_x = self.position[0] * PIXELS_PER_METER + x_offset
        bob_y = SCREEN_HEIGHT - (self.position[1] * PIXELS_PER_METER + y_offset)
        bob_pixel = (int(bob_x), int(bob_y))

        pygame.draw.line(screen, "white", pivot_pixel, bob_pixel, 2)
        pygame.draw.circle(screen, "white", pivot_pixel, 5)
        pygame.draw.circle(screen, "white", bob_pixel, self.bob_radius)
