'''
Firing Bullets
In AlienInvasion, we need to modify _check_keydown_events() to fire a bullet when the player
presses the spacebar. We don’t need to change _check_keyup _events() because nothing happens when
the spacebar is released. We also need to modify _update_screen() to make sure each bullet is drawn
to the screen before we call flip().

We know there will be a bit of work to do when we fire a bullet, so let’s write a new method,
_fire_bullet(), to handle this work:
'''

import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet #1

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE: #2
            self._fire_bullet()
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self) #3
        self.bullets.add(new_bullet) #4

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites(): #5
            bullet.draw_bullet()
        pygame.display.flip()

if __name__ == '__main__':
       # Make a game instance, and run the game.
       ai = AlienInvasion()
       ai.run_game()

'''
First, we import Bullet #1. Then we call _fire_bullet() when the space­ bar is pressed #2. 
In _fire_bullet(), we make an instance of Bullet and call it new_bullet #3. We then add it to the 
group bullets using the add() method #4. The add() method is similar to append(), but it’s a 
method that’s written spe­ cifically for Pygame groups.

The bullets.sprites() method returns a list of all sprites in the group bullets. To draw all 
fired bullets to the screen, we loop through the sprites in bullets and call draw_bullet() on 
each one #5.

When you run alien_invasion.py now, you should be able to move the ship right and left, and fire 
as many bullets as you want. The bullets travel up the screen and disappear when they reach the 
top. You can alter the size, color, and speed of the bullets in 
settings.py.
'''

