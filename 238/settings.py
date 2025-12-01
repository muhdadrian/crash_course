'''
Adjusting the Ship’s Speed
Currently, the ship moves one pixel per cycle through the while loop, but we can take finer
control of the ship’s speed by adding a ship_speed attribute to the Settings class. We’ll use
this attribute to determine how far to move the ship on each pass through the loop. Here’s the
new attribute in settings.py:
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

'''
We set the initial value of ship_speed to 1.5. When the ship moves now, its position is adjusted 
by 1.5 pixels rather than 1 pixel on each pass through the loop.

We’re using decimal values for the speed setting to give us finer control of the ship’s speed 
when we increase the tempo of the game later on. However, rect attributes such as x store only 
integer values, so we need to make some modifications to Ship in 239:
'''
