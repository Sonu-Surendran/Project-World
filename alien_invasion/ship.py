import pygame

class Ship:
    """Class will manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set it's starting position"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #To load the ship into the game
        self.image = pygame.image.load("Images/Space_Ship/space_ship_image.bmp")
        self.image_rect = self.image.get_rect()

        #defining the default location of the ship at the bottom of center
        self.image_rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at the current location"""
        self.screen.blit(self.image, self.image_rect)