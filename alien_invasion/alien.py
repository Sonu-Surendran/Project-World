import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position"""

        super().__init__()
        self.screen = ai_game.screen
        #Load alien space image
        self.image = pygame.image.load("Images/Space_Ship/enemy_ship.bmp")
        self.image = pygame.transform.scale(self.image, (75, 60))
        self.rect = self.image.get_rect()
        self.speed = ai_game.settings.alien_ship_speed

        #Start each new alien at the top left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store alien horizontal position
        self.x_axis = float(self.rect.x)

    def update(self):
        self.x_axis += self.speed
        self.rect.x = self.x_axis