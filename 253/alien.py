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

       def update(self):
           """Move the alien to the right."""
           self.x += self.settings.alien_speed #1
           self.rect.x = self.x #2

'''
We create a settings parameter in __init__() so we can access the alien’s speed in update(). Each 
time we update an alien’s position, we move it to the right by the amount stored in alien_speed. 
We track the alien’s exact position with the self.x attribute, which can hold decimal values #1. 
We then use the value of self.x to update the position of the alien’s rect #2.

In the main while loop, we already have calls to update the ship and bullet positions.
'''
