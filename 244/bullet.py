'''
Here’s the second part of bullet.py, update() and draw_bullet():
'''

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed #1
        # Update the rect position.
        self.rect.y = self.y #2

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect) #3

'''
The update() method manages the bullet’s position. When a bullet is fired, it moves up the screen, 
which corresponds to a decreasing y-coordinate value. To update the position, we subtract the 
amount stored in settings .bullet_speed from self.y #1. We then use the value of self.y to set the 
value of self.rect.y #2.

The bullet_speed setting allows us to increase the speed of the bullets as the game progresses or 
as needed to refine the game’s behavior. Once a bullet is fired, we never change the value of its 
x-coordinate, so it will travel vertically in a straight line even if the ship moves.

When we want to draw a bullet, we call draw_bullet(). The draw.rect() function fills the part of 
the screen defined by the bullet’s rect with the color stored in self.color #3.
'''

