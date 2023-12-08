import pygame
from object import *

class Obstacle(Object):
    def __init__(self, pos, size, image, group, speed):
        super().__init__(pos, size, image, group)
#how fast sprite moves across screen
        self.speed = speed

    def moveObstacle(self):
        x = self.pos[0]
        y = self.pos[1]

        x += self.speed
#keeps sprites from moving infinitely (length of screen) makes it look like there is a long row of logs/cars rather than teleporting
        if x >= 48*15:
            x = -48
        if x <= 48 * -2:

        self.pos = (x,y)

    def update(self):
        self.setImage()
        self.moveObstacle()


