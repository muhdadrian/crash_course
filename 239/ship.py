
import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game): #1
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship2.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position. #2
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's x value, not the rect.
        if self.moving_right:
            self.x += self.settings.ship_speed #3
        if self.moving_left:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x #4

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

'''
We create a settings attribute for Ship, so we can use it in update() #1. Because we’re adjusting 
the position of the ship by fractions of a pixel, we need to assign the position to a variable that 
can store a decimal value. You can use a decimal value to set an attribute of rect, but the rect 
will only keep the integer portion of that value. To keep track of the ship’s position accurately, 
we define a new self.x attribute that can hold decimal values #2. We use the float() function to 
convert the value of self.rect.x to a decimal and assign this value to self.x.

Now when we change the ship’s position in update(), the value of self.x is adjusted by the amount 
stored in settings.ship_speed #3. After self.x has been updated, we use the new value to update 
self.rect.x, which controls the position of the ship #4. Only the integer portion of self.x will 
be stored in self.rect.x, but that’s fine for displaying the ship.

Now we can change the value of ship_speed, and any value greater than one will make the ship move 
faster. This will help make the ship respond quickly enough to shoot down aliens, and it will let 
us change the tempo of the game as the player progresses in gameplay.
'''

'''
If you’re using macOS, you might notice that the ship moves very slowly, even with a high speed 
setting. You can remedy this problem by running the game in fullscreen mode, which we’ll implement 
shortly.
'''
