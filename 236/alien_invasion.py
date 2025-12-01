'''
Piloting the Ship
Next, we’ll give the player the ability to move the ship right and left. We’ll write code that
responds when the player presses the right or left arrow key. We’ll focus on movement to the right
first, and then we’ll apply the same prin­ ciples to control movement to the left. As we add
this code, you’ll learn how to control the movement of images on the screen and respond to user
input.

Responding to a Keypress
Whenever the player presses a key, that keypress is registered in Pygame as an event. Each event is
picked up by the pygame.event.get() method. We need to specify in our _check_events() method what
kind of events we want the game to check for. Each keypress is registered as a KEYDOWN event.

When Pygame detects a KEYDOWN event, we need to check whether the key that was pressed is one that
triggers a certain action. For example, if the player presses the right arrow key, we want to
increase the ship’s rect.x value to move the ship to the right:
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

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN: #1
                if event.key == pygame.K_RIGHT: #2
                    # Move the ship to the right.
                    self.ship.rect.x += 1 #3

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
Inside _check_events() we add an elif block to the event loop to respond when Pygame detects a 
KEYDOWN event #1. We check whether the key pressed, event.key, is the right arrow key #2. The right 
arrow key is represented by pygame.K_RIGHT. If the right arrow key was pressed, we move the ship 
to the right by increasing the value of self.ship.rect.x by 1 #3.

When you run alien_invasion.py now, the ship should move to the right one pixel every time you 
press the right arrow key. That’s a start, but it’s not an efficient way to control the ship. 
Let’s improve this control by allowing continuous movement.
'''






