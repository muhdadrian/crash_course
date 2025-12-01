# Checking Whether an Alien Has Hit the Edge

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
       """A class to represent a single alien in the fleet."""

       def __init__(self, ai_game):
           """Initialize the alien and set its starting position."""
           super().__init__()
           self.screen = ai_game.screen
           self.settings = ai_game.settings

           # Load the alien image and set its rect attribute.
           self.image = pygame.image.load('images/alien.bmp')
           self.rect = self.image.get_rect()

           # Start each new alien near the top left of the screen.
           self.rect.x = self.rect.width
           self.rect.y = self.rect.height

           # Store the alien's exact horizontal position.
           self.x = float(self.rect.x)

       def check_edges(self):
           """Return True if alien is at edge of screen."""
           screen_rect = self.screen.get_rect()
           if self.rect.right >= screen_rect.right or self.rect.left <= 0: #1
               return True

       def update(self):
            """Move the alien right or left."""
            self.x += (self.settings.alien_speed * self.settings.fleet_direction) #2
            self.rect.x = self.x

'''
We can call the new method check_edges() on any alien to see whether it’s at the left or right 
edge. The alien is at the right edge if the right attri- bute of its rect is greater than or equal
to the right attribute of the screen’s rect. It’s at the left edge if its left value is less than 
or equal to 0 #1.

We modify the method update() to allow motion to the left or right by multiplying the alien’s 
speed by the value of fleet_direction #2. If fleet _direction is 1, the value of alien_speed will 
be added to the alien’s current position, moving the alien to the right; if fleet_direction is −1,
the value will be subtracted from the alien’s position, moving the alien to the left.
'''