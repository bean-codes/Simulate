import pygame
from pygame.locals import *
import random


BLUE = (0, 0, 255)

class Entity:
    def __init__(self, x, y, size):  
        self.x = x
        self.y = y
        self.size = size
        self.color = BLUE
        self.thickness = 1


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y),
                            self.size, self.thickness)



class RandEnt:
    def __init__(self):
        self.height = 400
        self.width = 300
        self.size = random.randint(15, 25)
        self.x = random.randint(self.size, self.width - self.size)
        self.y = random.randint(self.size, self.height - self.size)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.thickness = 0


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y),
                            self.size, self.thickness)