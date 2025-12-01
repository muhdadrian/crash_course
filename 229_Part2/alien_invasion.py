'''
Starting the Game Project
We’ll begin building the game by creating an empty Pygame window. Later, we’ll draw the game
elements, such as the ship and the aliens, on this window. We’ll also make our game respond to
user input, set the background color, and load a ship image.

Creating a Pygame Window and Responding to User Input
We’ll make an empty Pygame window by creating a class to represent the game.
'''

import sys

import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init() #1

        self.screen = pygame.display.set_mode((1200, 800)) #2
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""
        while True: #3
            # Watch for keyboard and mouse events.
            for event in pygame.event.get(): #4
                if event.type == pygame.QUIT: #5
                    sys.exit()

            # Make the most recently drawn screen visible.
            pygame.display.flip() #6

if __name__ == '__main__':
       # Make a game instance, and run the game.
       ai = AlienInvasion()
       ai.run_game()

'''
First, we import the sys and pygame modules. The pygame module contains the functionality we 
need to make a game. We’ll use tools in the sys module to exit the game when the player quits.
Alien Invasion starts as a class called AlienInvasion. In the __init__() method, the pygame.init() 
function initializes the background settings that Pygame needs to work properly #1. At #2, we call 
pygame.display.set_mode() to create a display window, on which we’ll draw all the game’s graphical 
elements. The argument (1200, 800) is a tuple that defines the dimensions of the game window, 
which will be 1200 pixels wide by 800 pixels high. (You can adjust these values depending on your 
display size.) We assign this display window to the attribute self.screen, so it will be 
available in all methods in the class.

The object we assigned to self.screen is called a surface. A surface in Pygame is a part of the 
screen where a game element can be displayed. Each element in the game, like an alien or a ship, 
is its own surface. The surface returned by display.set_mode() represents the entire game window. 
When we activate the game’s animation loop, this surface will be redrawn on every pass through 
the loop, so it can be updated with any changes triggered by user input.

The game is controlled by the run_game() method. This method contains a while loop #3 that runs 
continually. The while loop contains an event loop and code that manages screen updates. An event 
is an action that the user performs while playing the game, such as pressing a key or moving the 
mouse. To make our program respond to events, we write this event loop to listen for events and 
perform appropriate tasks depending on the kinds of events that occur. The for loop at #4 is an 
event loop.

To access the events that Pygame detects, we’ll use the pygame.event .get() function. This function 
returns a list of events that have taken place since the last time this function was called. Any 
keyboard or mouse event will cause this for loop to run. Inside the loop, we’ll write a series of 
if statements to detect and respond to specific events. For example, when the player clicks the game 
window’s close button, a pygame.QUIT event is detected and we call sys.exit() to exit the game #5.

The call to pygame.display.flip() at #6 tells Pygame to make the most recently drawn screen visible. 
In this case, it simply draws an empty screen on each pass through the while loop, erasing the old 
screen so only the new screen is visible. When we move the game elements around, 
pygame.display.flip() continually updates the display to show the new positions of game elements 
and hides the old ones, creating the illusion of smooth movement.

At the end of the file, we create an instance of the game, and then call run_game(). We place 
run_game() in an if block that only runs if the file is called directly. When you run this 
alien_invasion.py file, you should see an empty Pygame window.
'''