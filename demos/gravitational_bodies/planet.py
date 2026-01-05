import pygame
import numpy as np
from physical_object import PhysicalObject
from constants import PIXELS_PER_METER, G, SCREEN_HEIGHT

class Planet(PhysicalObject):
    def __init__(self, position, velocity, mass, radius):
        super().__init__(position, velocity, mass, radius)

    def draw(self, screen, offset):
        x, y = self.position
        x_offset, y_offset = offset
        x_pixel, y_pixel = x * PIXELS_PER_METER + x_offset, y * PIXELS_PER_METER + y_offset
        y_pixel = SCREEN_HEIGHT - y_pixel
        draw_position = (x_pixel, y_pixel)
        print(draw_position)
        pygame.draw.circle(screen, "white", draw_position, self.radius, 5)

    def update(self, dt, bodies):
        def calculate_force(body):
            self_pos = np.array(self.position)
            other_pos = np.array(body.get_position())
            r = other_pos - self_pos
            
            distance = np.linalg.norm(r)

            r_unit = r / distance
            
            F_magnitude = G * body.get_mass() * self.mass / distance ** 2
            
            return F_magnitude * r_unit


        F_total = np.zeros(2)

        for body in bodies:
            F_total += calculate_force(body)

        acceleration = F_total / self.mass

        x, y = self.position
        vx, vy = self.velocity
        ax, ay = acceleration
        
        x += vx * dt
        y += vy * dt
        self.position = (x, y)
        
        vx += ax * dt
        vy += ay * dt
        self.velocity = (vx, vy)



    def get_mass(self):
        return self.mass

    def get_position(self):
        return self.position
