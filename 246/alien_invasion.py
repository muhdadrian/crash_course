'''
Deleting Old Bullets
At the moment, the bullets disappear when they reach the top, but only because Pygame can’t draw
them above the top of the screen. The bullets actually continue to exist; their y-coordinate
values just grow increasingly negative. This is a problem, because they continue to consume memory
and processing power.

We need to get rid of these old bullets, or the game will slow down from doing so much unnecessary
work. To do this, we need to detect when the bottom value of a bullet’s rect has a value of 0,
which indicates the bullet has passed off the top of the screen:
'''

'''
When you use a for loop with a list (or a group in Pygame), Python expects that the list will stay
the same length as long as the loop is running. Because we can’t remove items from a list or 
group within a for loop, we have to loop over a copy of the group. We use the copy() method to set
up the for loop #1, which enables us to modify bullets inside the loop. We check each bullet to see 
whether it has disappeared off the top of the screen at #2. If it has, we remove it from 
bullets #3. At #4 we insert a print() call to show how many bullets currently exist in the game and
verify that they’re being deleted when they reach the top of the screen.

If this code works correctly, we can watch the terminal output while firing bullets and see 
that the number of bullets decreases to zero after each series of bullets has cleared the top of 
the screen. After you run the game and verify that bullets are being deleted properly, remove the 
print() call. If you leave it in, the game will slow down significantly because it takes more time
to write output to the terminal than it does to draw graphics to the game window.
'''

import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

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

            # Get rid of bullets that have disappeared.
            for bullet in self.bullets.copy(): #1
                if bullet.rect.bottom <= 0: #2
                    self.bullets.remove(bullet) #3
            print(len(self.bullets)) #4

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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

if __name__ == '__main__':
       # Make a game instance, and run the game.
       ai = AlienInvasion()
       ai.run_game()

