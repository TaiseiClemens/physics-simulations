import pygame
import numpy as np
from constants import SCREEN_HEIGHT, PIXELS_PER_METER

class Disk:
    def __init__(self, position, velocity, mass, radius):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.radius = radius * PIXELS_PER_METER

    def draw(self, screen, offset):
        x, y = self.position
        x_offset, y_offset = offset
        x_pixel, y_pixel = x * PIXELS_PER_METER + x_offset, y * PIXELS_PER_METER + y_offset
        y_pixel = SCREEN_HEIGHT - y_pixel
        draw_position = (x_pixel, y_pixel)
        print(draw_position)
        pygame.draw.circle(screen, "white", draw_position, self.radius, 5)

    def update(self, dt, disks):

        p_1 = np.array(self.position)
        v_1 = np.array(self.velocity)
        for disk in disks:
            p_2 = np.array(disk.get_position())
            if np.linalg.norm(p_2 - p_1) * PIXELS_PER_METER < self.radius * 2:
                # Has collided
                print("Collided!")
                v_2 = np.array(disk.get_velocity())

                normal_unit = (p_2 - p_1)/np.linalg.norm(p_2 - p_1)
                v_1n = np.dot(v_1, normal_unit) # Normal Component
                v_1t = v_1 - v_1n * normal_unit # Tangential Component
                v_2n = np.dot(v_2, normal_unit)
                v_2t = v_2 - v_2n * normal_unit
                
                m_1 = self.mass
                m_2 = disk.get_mass()

                v_1n_prime = ((m_1 - m_2) * v_1n + 2 * m_2 * v_2n) / (m_1 + m_2)
                v_2n_prime = ((m_2 - m_1) * v_2n + 2 * m_1 * v_1n) / (m_1 + m_2)

                v_1_prime = v_1n_prime * normal_unit + v_1t
                v_2_prime = v_2n_prime * normal_unit + v_2t

                self.velocity = tuple(v_1_prime)
                disk.set_velocity(tuple(v_2_prime))

        x, y = self.position
        vx, vy = self.velocity

        x += vx * dt
        y += vy * dt
        self.position = (x, y)
                




    def get_position(self):
        return self.position
    def get_velocity(self):
        return self.velocity
    def get_mass(self):
        return self.mass
    def set_velocity(self, velocity):
        self.velocity = velocity
