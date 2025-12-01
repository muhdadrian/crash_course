'''
Refactoring: The _check_events() and _update_screen() Methods
In large projects, you’ll often refactor code you’ve written before adding more code. Refactoring
simplifies the structure of the code you’ve already written, making it easier to build on. In this
section, we’ll break the run_game() method, which is getting lengthy, into two helper methods. A
helper method does work inside a class but isn’t meant to be called through an instance. In Python,
a single leading underscore indicates a helper method.

The _check_events() Method
We’ll move the code that manages events to a separate method called _check_events(). This will
simplify run_game() and isolate the event management loop. Isolating the event loop allows you
to manage events separately from other aspects of the game, such as updating the screen.
Here’s the AlienInvasion class with the new _check_events() method, which only affects the code in
run_game():
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
            self._check_events() #1

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

if __name__ == '__main__':
       # Make a game instance, and run the game.
       ai = AlienInvasion()
       ai.run_game()

'''
We make a new _check_events() method #2 and move the lines that check whether the player has clicked 
to close the window into this new method.

To call a method from within a class, use dot notation with the variable self and the name of the 
method #1. We call the method from inside the while loop in run_game().

for update screen method: in 235
'''
