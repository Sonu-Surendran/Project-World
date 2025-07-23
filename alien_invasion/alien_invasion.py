import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall Class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        #Set the background colour
        self.bg_color = (self.settings.bg_color)

    def run_game(self):
        """Start the main loop the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullet()
            self._update_alien()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Watches for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyrelease_event(event)

    def _update_screen(self):
        """update the screen with latest drawings"""

        self.screen.fill(self.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)  
        #Make the most recently drawn screen visible
        pygame.display.flip()

    def _update_bullet(self):
        """Update the position of bullets and get rid of the old bullets"""
        self.bullets.update() 

        for bullet in self.bullets.copy():
            if bullet.bullet_rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_keydown_event(self, event):
        """Responses to keypress"""

        if event.key == pygame.K_RIGHT:
            self.ship.movement_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.movement_left = True
        elif event.key == pygame.K_q:
                sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyrelease_event(self, event):
        """Responses to key release"""

        if event.key == pygame.K_RIGHT:
            self.ship.movement_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.movement_left = False 

    def _fire_bullet(self):
        """"Generate bullet for each keystroke"""

        if self.settings.allowed_bullets >= len(self.bullets):
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)  

    def _create_fleet(self):
        """Generate the screen with enemy alien ships"""

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        current_x, current_y = alien_width, alien_height
        #Create aliens until there is no room left
        while current_y < (self.settings.screen_height - 10 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            
            #row value is reseted and height is increased
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_axis, y_axis):
        """Creating an alien and placing it in row"""
        new_alien = Alien(self)
        # new_alien.x = x_axis
        new_alien.rect.x = x_axis
        new_alien.rect.y = y_axis
        self.aliens.add(new_alien)

    def _update_alien(self):
        """Updates the position of the alien"""
        self.aliens.update()


if __name__ == '__main__':
    #Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()