import pygame

class Ship:
    """Class will manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set it's starting position"""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #To load the ship into the game
        self.image = pygame.image.load("Images/Space_Ship/space_ship_image.bmp")
        self.image_rect = self.image.get_rect()

        #defining the default location of the ship at the bottom of center
        self.image_rect.midbottom = self.screen_rect.midbottom

        #store the float value of the ship
        self.float_position = float(self.image_rect.x)

        #Movement Flag - changes based on the keypress
        self.movement_right = False
        self.movement_left = False

    def update(self):
        """Update the position of the ship based on the movenment flag"""

        if self.movement_right and self.image_rect.right < self.screen_rect.right:
            print(self.screen_rect.right)
            self.float_position += self.settings.ship_speed
        if self.movement_left and self.image_rect.left > 0:
            self.float_position -= self.settings.ship_speed

        self.image_rect.x = self.float_position

    def blitme(self):
        """Draw the ship at the current location"""
        self.screen.blit(self.image, self.image_rect)