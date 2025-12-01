# Creating a Row of Aliens

import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        while True:
            self.check_events()
            self.ship.update()
            self.update_bullets()
            self.update_screen()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    def fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self) #1
        alien_width = alien.rect.width #2
        available_space_x = self.settings.screen_width - (2 * alien_width) #3
        number_aliens_x = available_space_x // (2 * alien_width)

        # Create the first row of aliens.
        for alien_number in range(number_aliens_x): #4
            # Create an alien and place it in the row.
            alien = Alien(self)
            alien.x = alien_width + 2 * alien_width * alien_number #5
            alien.rect.x = alien.x
            self.aliens.add(alien)
    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

'''
We’ve already thought through most of this code. We need to know the alien’s width and height to 
place aliens, so we create an alien at #1 before we perform calculations. This alien won’t be part
of the fleet, so don’t add it to the group aliens. At #2 we get the alien’s width from its rect 
attribute and store this value in alien_width so we don’t have to keep working through the rect 
attribute. At #3 we calculate the horizontal space available for aliens and the number of aliens 
that can fit into that space.

Next, we set up a loop that counts from 0 to the number of aliens we need to make #4. In the main 
body of the loop, we create a new alien and then set its x-coordinate value to place it in the 
row #5. Each alien is pushed to the right one alien width from the left margin. Next, we multiply 
the alien width by 2 to account for the space each alien takes up, including the empty space to 
its right, and we multiply this amount by the alien’s position in the row. We use the alien’s 
x attribute to set the position of its rect. Then we add each new alien to the group aliens.
'''
