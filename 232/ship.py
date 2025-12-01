import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen #1
        self.screen_rect = ai_game.screen.get_rect() #2

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship2.bmp') #3
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom #4

        def blitme(self): #5
            """Draw the ship at its current location."""
            self.screen.blit(self.image, self.rect)

'''
Pygame is efficient because it lets you treat all game elements like rect angles (rects), even if 
they’re not exactly shaped like rectangles. Treating an element as a rectangle is efficient 
because rectangles are simple geometric shapes. When Pygame needs to figure out whether two 
game elements have collided, for example, it can do this more quickly if it treats each object 
as a rectangle. This approach usually works well enough that no one playing the game will notice 
that we’re not working with the exact shape of each game element. We’ll treat the ship and the 
screen as rectangles in this class.

We import the pygame module before defining the class. The __init__() method of Ship takes two 
parameters: the self reference and a reference to the current instance of the AlienInvasion class.
This will give Ship access to all the game resources defined in AlienInvasion. At #1 we assign the 
screen to an attribute of Ship, so we can access it easily in all the methods in this class. 
At #2 we access the screen’s rect attribute using the get_rect() method and assign it to 
self.screen_rect. Doing so allows us to place the ship in the correct location on the screen.

To load the image, we call pygame.image.load() #3 and give it the location of our ship image. 
This function returns a surface representing the ship, which we assign to self.image. When the 
image is loaded, we call get_rect() to access the ship surface’s rect attribute so we can later 
use it to place the ship.

When you’re working with a rect object, you can use the x and y coordinates of the top, 
bottom, left, and right edges of the rectangle, as well as the center, to place the object. You 
can set any of these values to establish the current position of the rect. When you’re centering a 
game element, work with the center, centerx, or centery attributes of a rect. When you’re working 
at an edge of the screen, work with the top, bottom, left, or right attributes. There are also 
attributes that combine these properties, such as midbottom, midtop, midleft, and midright. When 
you’re adjusting the horizontal or vertical placement of the rect, you can just use the x and y 
attributes, which are the x and y coordinates of its top left corner. These attributes 
spare you from having to do calculations that game developers formerly had to do manually, and 
you’ll use them often.

We’ll position the ship at the bottom center of the screen. To do so, make the value of 
self.rect.midbottom match the midbottom attribute of the screen’s rect #4. Pygame uses these rect 
attributes to position the ship image so it’s centered horizontally and aligned with the bottom of 
the screen.

At #5, we define the blitme() method, which draws the image to the screen at the position specified 
by self.rect.
'''

'''
In Pygame, the origin (0, 0) is at the top-left corner of the screen, and coordinates increase as 
you go down and to the right. On a 1200 by 800 screen, the origin is at the top-left corner, and 
the bottom-right corner has the coordinates (1200, 800). These coordinates refer to the game 
window, not the physical screen.
'''