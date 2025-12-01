'''
Creating a Settings Class
Each time we introduce new functionality into the game, we’ll typically create some new settings as
well. Instead of adding settings throughout the code, let’s write a module called settings that
contains a class called Settings to store all these values in one place. This approach allows us to
work with just one settings object any time we need to access an individual setting. This also makes
it easier to modify the game’s appearance and behavior as our project grows: to modify the game,
we’ll simply change some values in settings.py, which we’ll create next, instead of searching for
different settings throughout the project.

Create a new file named settings.py inside your alien_invasion folder, and add this initial
Settings class:
'''


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

'''
To make an instance of Settings in the project and use it to access our settings, we need to 
modify alien_invasion.py.
'''