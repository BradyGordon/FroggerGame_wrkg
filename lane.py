import random, pygame
from obstacle import *

class Lane:
    def __init__(self, pos, group, speed, lane_type):
        self.pos = pos
        self.group = group
        self.speed = speed
        self.lane_type = lane_type

        self.setupObstacles()
#obstabcles such as cars/logs/turles
    def setupObstacles(self):
        if self.speed > 0:
            self.direction = "right"
        else:
            self.direction = "left"
#making it either car png 1 or 2 thatll go across
        if self.lane_type == "streets":
            car = random.randint(1,2)
            image_directory = f"assets/{self.lane_type}/{self.direction}/{car}.png"
#creating position, speed and amount of cars per lane
            Obstacle(self.pos, (48, 48), image_directory, self.group, self.speed).setImage()
            Obstacle((self.pos[0] + 5*48, self.pos[1]), (48, 48), image_directory, self.group, self.speed).setImage()
            Obstacle((self.pos[0] + 10*48, self.pos[1]), (48, 48), image_directory, self.group, self.speed).setImage()

        elif self.lane_type == "river":
            if self.direction == "left":
                left, middle, right = f"assets/{self.lane_type}/{self.direction}/turtle.png", f"assets/{self.lane_type}/{self.direction}/turtle.png", f"assets/{self.lane_type}/{self.direction}/turtle.png"
            elif self.direction == "right":
                left, middle, right = f"assets/{self.lane_type}/{self.direction}/left(2).png", f"assets/{self.lane_type}/{self.direction}/middle.png", f"assets/{self.lane_type}/{self.direction}/right(2).png" #creating one full log using 3 pictures.
#river and declaring if it will be turtle or log placed across river. Along with this if it is a log that comes up it will place the position of the log together
            Obstacle(self.pos, (48, 48), left, self.group, self.speed).setImage()
            Obstacle((self.pos[0] + 48, self.pos[1]), (48, 48), middle, self.group, self.speed).setImage()
            Obstacle((self.pos[0] + 2*48, self.pos[1]), (48, 48), right, self.group, self.speed).setImage()


            Obstacle((self.pos[0] + 7*48, self.pos[1]), (48, 48), left, self.group, self.speed).setImage()
            Obstacle((self.pos[0] + 8*48, self.pos[1]), (48, 48), middle, self.group, self.speed).setImage()
            Obstacle((self.pos[0] + 9*48, self.pos[1]), (48, 48), right, self.group, self.speed).setImage()