'''
Moving Both Left and Right
Now that the ship can move continuously to the right, adding movement to the left is
straightforward. Again, we’ll modify the Ship class and the _check _events() method. Here are the
relevant changes to __init__() and update() in Ship:
'''


import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship2.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

'''
In __init__(), we add a self.moving_left flag. In update(), we use two separate if blocks rather 
than an elif to allow the ship’s rect.x value to be increased and then decreased when both arrow 
keys are held down. This results in the ship standing still. If we used elif for motion to the 
left, the right arrow key would always have priority. Doing it this way makes the movements more 
accurate when switching from right to left when the player might momentarily hold down both keys.

We have to make two adjustments to _check_events() in alien_invasion.py:
'''
