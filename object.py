import pygame

#setting paraemeters for how all objects and sprites will function throughout game
class Object(pygame.sprite.Sprite):
    def __init__(self, pos, size, image, group):
        super().__init__(group)

        self.pos = pos
        self.size = size

        self.image_directory = image_directory
#
    def setImage(self):
        self.image = pygame.image.load(self.image_directory)
        self.image = pygame.transform.scale(self.image, self.size)
        self.surf = pygame.Surface(self.size).covert_alpha()
        self.surf.fill((0,0,0,0)) #gets rid of transparaent pixels
        self.rect = self.surf.get_rect(topleft = self.pos) #top left of sprite will be on top left of screen at 0 0
        self.surf.blit(self.image, (0,0))

    def update(self):
        self.setImage()