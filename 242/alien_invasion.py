'''
Running the Game in Fullscreen Mode
Pygame has a fullscreen mode that you might like better than running the game in a regular window.
Some games look better in fullscreen mode, and macOS users might see better performance in
fullscreen mode.

To run the game in fullscreen mode, make the following changes in __init__():
'''

import sys

import pygame

from settings import Settings
from ship import Ship
class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) #1
        self.settings.screen_width = self.screen.get_rect().width #2
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
       # Make a game instance, and run the game.
       ai = AlienInvasion()
       ai.run_game()

'''
When creating the screen surface, we pass a size of (0, 0) and the parameter pygame.FULLSCREEN #1. 
This tells Pygame to figure out a window size that will fill the screen. Because we don’t know 
the width and height of the screen ahead of time, we update these settings after the screen is 
created #2. We use the width and height attributes of the screen’s rect to update the settings 
object.
If you like how the game looks or behaves in fullscreen mode, keep these settings. If you liked 
the game better in its own window, you can revert back to the original approach where we set a 
specific screen size for the game.
'''

'''
Make sure you can quit by pressing Q before running the game in fullscreen mode; Pygame offers no 
default way to quit a game while in fullscreen mode.
'''