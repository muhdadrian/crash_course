'''
Allowing Continuous Movement
When the player holds down the right arrow key, we want the ship to continue moving right until
the player releases the key. We’ll have the game detect a pygame.KEYUP event so we’ll know when
the right arrow key is released; then we’ll use the KEYDOWN and KEYUP events together with a flag
called moving_right to implement continuous motion.

When the moving_right flag is False, the ship will be motionless. When the player presses the
right arrow key, we’ll set the flag to True, and when the player releases the key, we’ll set the
flag to False again.

The Ship class controls all attributes of the ship, so we’ll give it an attribute called
moving_right and an update() method to check the status of the moving_right flag. The update() method will change the position of the ship if the flag is set to True. We’ll call this method once on each pass through the while loop to update the position of the ship.

Here are the changes to Ship:
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
        self.moving_right = False #1

    def update(self): #2
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

'''
We add a self.moving_right attribute in the __init__() method and set it to False initially #1. 
Then we add update(), which moves the ship right if the flag is True #2. The update() method will
be called through an instance of Ship, so it’s not considered a helper method.
'''