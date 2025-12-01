'''
Limiting the Ship’s Range
At this point, the ship will disappear off either edge of the screen if you hold down an arrow
key long enough. Let’s correct this so the ship stops moving when it reaches the screen’s edge.
We do this by modifying the update() method in Ship:
'''

import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship2.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right: #1
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0: #2
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

'''
This code checks the position of the ship before changing the value of self.x. The code 
self.rect.right returns the x-coordinate of the right edge of the ship’s rect. If this value is 
less than the value returned by self.screen _rect.right, the ship hasn’t reached the right edge 
of the screen #1. The same goes for the left edge: if the value of the left side of the rect is 
greater than zero, the ship hasn’t reached the left edge of the screen #2. This ensures the ship is 
within these bounds before adjusting the value of self.x.
When you run alien_invasion.py now, the ship should stop moving at either edge of the screen. 
This is pretty cool; all we’ve done is add a conditional test in an if statement, but it 
feels like the ship hits a wall or a force field at either edge of the screen!
'''

