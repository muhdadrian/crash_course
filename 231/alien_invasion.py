
import sys

import pygame

from settings import Settings
class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings() #1

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) #2
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color) #3

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
       # Make a game instance, and run the game.
       ai = AlienInvasion()
       ai.run_game()

'''
We import Settings into the main program file. Then we create an instance of Settings and assign it 
to self.settings #1, after making the call to pygame.init(). When we create a screen #2, we use the 
screen_width and screen_height attributes of self.settings, and then we use self.settings to 
access the background color when filling the screen at #3 as well.

When you run alien_invasion.py now you won’t yet see any changes, because all we’ve done is move 
the settings we were already using elsewhere. Now we’re ready to start adding new elements to 
the screen.
'''
