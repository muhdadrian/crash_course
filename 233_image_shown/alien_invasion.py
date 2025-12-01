'''
Drawing the Ship to the Screen
Now let’s update alien_invasion.py so it creates a ship and calls the ship’s blitme() method:
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

        self.ship = Ship(self) #1

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme() #2

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
       # Make a game instance, and run the game.
       ai = AlienInvasion()
       ai.run_game()

'''
We import Ship and then make an instance of Ship after the screen has been created #1. The call to
Ship() requires one argument, an instance of AlienInvasion. The self argument here refers to the 
current instance of AlienInvasion. This is the parameter that gives Ship access to the game’s 
resources, such as the screen object. We assign this Ship instance to self.ship.

After filling the background, we draw the ship on the screen by calling ship.blitme(), so the ship 
appears on top of the background #2.

When you run alien_invasion.py now, you should see an empty game screen with the rocket ship 
sitting at the bottom center, as shown in the displayed window.
'''
