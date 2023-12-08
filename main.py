import pygame, sys, random
from object import *
from frog import *
from lane import *

#set up of how large the screen is, color of backgrounds, etc
class Game:
    def __init__(self, screen_dimesions, screen_caption, screen_color):
        pygame.init()
        pygame.display.set_mode(screen_dimensions)
        pygame.display.set_caption(screen_caption)

        self.screen_color = screen_color
        self.DISPLAY = pygame.display.get_surface()

        #sprite group with all the different types of sprites and then stored together in all group
        self.objective_group = pygame.sprite.Group()
        self.car_group = pygame.sprite.Group()
        self.river_group = pygame.sprite.Group()
        self.frog_group = pygame.sprite.Group()

        self.all_groups = [self.objective_group, self.car_group, self.river_group, self.frog_group]

        self.river_speeds = {}
        self.assetSetup()

    def assetSetup(self):
        Object((0,0), (672,768, "assets/background.png", self.objective_group)) #creates background blue/black

        for x in range(14): #creating strips of both purple and green grass across
            Object((x*48, 384), (48,48), "assets/grass/purple.png", self.objective_group)
            Object((x*48, 672), (48,48), "assets/grass/purple.png", self.objective_group)
        for x in range(28):
            Object((x*24, 72), (24,72), "assets/grass/green.png", self.objective_group) #green grass png is twice the length so requires half the amount of pixels

        #lanes negative value moves towards right side of screen postive left. higher the number the faster it is giving differents looks of speed in each lane
        speeds = [-1.25, -1, -.75, -.5, -.25, .25, .5, .75, 1, 1.25]
        random.shuffle(speeds)

        #river lanes
        for y in range(5):
            y_pos = y*48 + 144
            new_lane = Lane((0, y_pos), self.river_group, speeds.pop(), "river") #creating random speeds for each river lane/group
            self.river_group[y_pos//48] = new_lane.speed

        #street lanes same concept as river just different position
        for y in range(5):
            y_pos = y*48 + 432
            Lane((0, y_pos), self.car_group, speeds.pop(), "streets")


#frog position middle on bottom as well as how the frog will interact with obstacles on course as well as contains collision groups things which will kill it and how it will interact with these items

        self.frog = Frog((336,672), (48,48), "assets/frog/up.png", self.frog_group, [self.car_group, self.river_group], self.river_speeds)

#
    def run(self):
        while True:
            self.DISPLAY.fill(self.screen_color)
#making it so you move when pressing wasd keys for frog class
            self.frog.keyups = []
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
                    sys.exit()
                elif event.type == pygame.KEYUP:
                    self.frog.keyups.append(event.key)

            for group in self.all_groups:
                for sprite in group:
                    sprite.update()

                group.draw(self.DISPLAY)

            pygame.display.update()

#screen size
game = Game((672,768)), "Frogger!!", (0,0,0)