class Settings:
    """A class to store all settings for Alien invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        #Display settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.ship_speed = 1.0

        #Bullet Settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 126, 0)
        self.allowed_bullets = 3