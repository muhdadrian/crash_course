'''
Limiting the Number of Bullets
Many shooting games limit the number of bullets a player can have on the screen at one time; doing
so encourages players to shoot accurately. We’ll do the same in Alien Invasion.

First, store the number of bullets allowed in settings.py: #1
'''

'''
This limits the player to three bullets at a time. We’ll use this setting in AlienInvasion to check 
how many bullets exist before creating a new bullet in _fire_bullet() in 247:
'''

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3 #1


