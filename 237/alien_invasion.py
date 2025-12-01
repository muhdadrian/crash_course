'''
Now we need to modify _check_events() so that moving_right is set to True when the right arrow
key is pressed and False when the key is released:
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

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update() #3
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
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True #1
            elif event.type == pygame.KEYUP: #2
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False


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
At #1, we modify how the game responds when the player presses the right arrow key: instead of 
changing the ship’s position directly, we merely set moving_right to True. At #2, we add a new elif 
block, which responds to KEYUP events. When the player releases the right arrow key (K_RIGHT), we 
set moving_right to False.
'''

'''
Next, we modify the while loop in run_game() so it calls the ship’s update() method on each pass 
through the loop #3.
'''

'''
The ship’s position will be updated after we’ve checked for keyboard events and before we update 
the screen. This allows the ship’s position to be updated in response to player input and ensures 
the updated position will be used when drawing the ship to the screen.

When you run alien_invasion.py and hold down the right arrow key, the ship should move continuously 
to the right until you release the key.
'''





