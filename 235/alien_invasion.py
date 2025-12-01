'''
The _update_screen() Method
To further simplify run_game(), we’ll move the code for updating the screen to a separate method
called _update_screen():
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
            self._update_screen()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

    def _check_events(self): #2
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
       # Make a game instance, and run the game.
       ai = AlienInvasion()
       ai.run_game()

"""
We moved the code that draws the background and the ship and flips the screen to _update_screen(). 
Now the body of the main loop in run_game() is much simpler. It’s easy to see that we’re looking 
for new events and updating the screen on each pass through the loop.

If you’ve already built a number of games, you’ll probably start out by breaking your code into 
methods like these. But if you’ve never tackled a project like this, you probably won’t know how 
to structure your code. This approach of writing code that works and then restructuring it as it 
grows more complex gives you an idea of a realistic development process: you start out writing 
your code as simply as possible, and then refactor it as your proj- ect becomes more complex.

Now that we’ve restructured the code to make it easier to add to, we can work on the dynamic 
aspects of the game!

"""









