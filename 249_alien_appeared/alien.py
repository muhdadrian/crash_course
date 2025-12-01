# Creating the Alien Class

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
       """A class to represent a single alien in the fleet."""

       def __init__(self, ai_game):
           """Initialize the alien and set its starting position."""
           super().__init__()
           self.screen = ai_game.screen

           # Load the alien image and set its rect attribute.
           self.image = pygame.image.load('images/alien.bmp')
           self.rect = self.image.get_rect()

           # Start each new alien near the top left of the screen.
           self.rect.x = self.rect.width #1
           self.rect.y = self.rect.height

           # Store the alien's exact horizontal position.
           self.x = float(self.rect.x) #2

'''
Most of this class is like the Ship class except for the aliens’ placement on the screen. We 
initially place each alien near the top-left corner of the screen; we add a space to the left of it
that’s equal to the alien’s width and a space above it equal to its height #1 so it’s easy to see. 
We’re mainly concerned with the aliens’ horizontal speed, so we’ll track the horizontal position 
of each alien precisely #2.

This Alien class doesn’t need a method for drawing it to the screen; instead, we’ll use a Pygame 
group method that automatically draws all the elements of a group to the screen.
'''