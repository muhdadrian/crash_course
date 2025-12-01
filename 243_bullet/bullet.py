'''
Creating the Bullet Class
Now create a bullet.py file to store our Bullet class. Here’s the first part of bullet.py:
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
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, #1
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop #2

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y) #3

'''
The Bullet class inherits from Sprite, which we import from the pygame .sprite module. When you use
sprites, you can group related elements in your game and act on all the grouped elements at once. 
To create a bullet instance, __init__() needs the current instance of AlienInvasion, and we call 
super() to inherit properly from Sprite. We also set attributes for the screen and settings 
objects, and for the bullet’s color.

At #1, we create the bullet’s rect attribute. The bullet isn’t based on an image, so we have to 
build a rect from scratch using the pygame.Rect() class. This class requires the x- and 
y-coordinates of the top-left corner of the rect, and the width and height of the rect. We 
initialize the rect at (0, 0), but we’ll move it to the correct location in the next line, because 
the bullet’s position depends on the ship’s position. We get the width and height of the bullet 
from the values stored in self.settings.

At #2, we set the bullet’s midtop attribute to match the ship’s midtop attribute. This will 
make the bullet emerge from the top of the ship, making it look like the bullet is fired from the 
ship. We store a decimal value for the bullet’s y-coordinate so we can make fine adjustments to 
the bullet’s speed #3.
'''
