import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullet fired from ship"""

    def __init__(self, ai_game):
        """Creating a bullet object at the ship's current position"""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #manifesting a bullet and defining it's position
        self.bullet_rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.bullet_rect.midtop = ai_game.ship.image_rect.midtop
        self.bullet_rect.x -= 5

        #storing bullet position
        self.bullet_yaxis = float(self.bullet_rect.y)

    def update(self):
        """Move the bullet up the screen"""

        #Update the exact position of the bullet
        self.bullet_yaxis -= self.settings.bullet_speed

        #update the rect position
        self.bullet_rect.y = self.bullet_yaxis

    def draw_bullet(self):
        """Draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.bullet_rect)