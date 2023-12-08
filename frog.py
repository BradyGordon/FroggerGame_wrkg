import pygame
from object import *

class Frog(Object):
    def __init__(self, pos, size, image, group, collision_groups, river_speeds):
        super().__init__(pos, size, image, group)

        self.keyups = []

        self.collision_groups = collision_groups

        self.river_speeds = river_speeds
        self.x_speed = 0

    def moveFrog(self):
        x = self.pos[0]
        y = self.pos[1]
#if the arrow key example UP is in the keyup function it will move the frog that direction
        if pygame.K_UP in self.keyups:
            self.image_directory = "assets/frog/up.png"
            y -= 48

        if pygame.K_DOWN in self.keyups:
            self.image_directory = "assets/frog/down.png"
            y += 48

        if pygame.K_LEFT in self.keyups:
            self.image_directory = "assets/frog/left.png"
            x -= 48

        if pygame.K_RIGHT in self.keyups:
            self.image_directory = "assets/frog/right.png"
            x += 48
#these speeds are off the screen to kill frog if it goes off
        x += self.x_speed
        if x <= -48 or x > 48*14 or y > 48*16:
            self.killFrog()
            return

        self.pos = (x,y)

    def checkCollisions(self):
        self.setImage()
#if the sprite is colliding with something it will switch to true and how the frog now interacts.
        collided = False
        for sprite_group in self.collision_groups:
            if pygame.sprite.spritecollideany(self, sprite_group):
                collided = True
#if speed becomes 8 it means you are either on log or in water. if in water it will kill frog and if it is colliding with log it will move it the same speed as log
        lane = self.pos[1]//48
        if collided:
            if lane < 8:
                self.x_speed = self.river_speeds[lane]
            else:
                self.killFrog()
        else:
            self.x_speed = 0
            if lane < 8:
                self.killFrog()

#if frog moves off screen it will kill frog/relocate to spawn
    def killFrog():
        self.x_speed = 0
        self.pos(336, 672)
        self.image_directory = "assets/frog/up.png"
        self.setImage()

    def update(self):
        self.setImage()
        self.moveFrog()
        self.checkCollisions()