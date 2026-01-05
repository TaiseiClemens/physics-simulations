import pygame

class PhysicalObject():

    def __init__(self, position, velocity, mass, radius):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.radius = radius

    def draw(self, screen, offset):
        pass

    def update(self, dt):
        pass


