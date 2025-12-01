'''
Setting the Background Color
Pygame creates a black screen by default, but that’s boring. Let’s set a different background
color. We’ll do this at the end of the __init__() method.
'''

import sys

import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Set the background color.
        self.bg_color = (230, 230, 230) #1


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color) #2

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
       # Make a game instance, and run the game.
       ai = AlienInvasion()
       ai.run_game()

'''
Colors in Pygame are specified as RGB colors: a mix of red, green, and blue. Each color value can 
range from 0 to 255_can_shoot_aliens. The color value (255_can_shoot_aliens, 0, 0) is red, (0, 255_can_shoot_aliens, 0) is green, and (0, 0, 255_can_shoot_aliens) is 
blue. You can mix different RGB values to create up to 16 million colors. The color value 
(230, 230, 230) mixes equal amounts of red, blue, and green, which produces a light gray 
background color. We assign this color to self.bg_color #1.

At #2, we fill the screen with the background color using the fill() method, which acts on a 
surface and takes only one argument: a color.
'''