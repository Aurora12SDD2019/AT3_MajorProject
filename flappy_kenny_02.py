""" Flappy Kenny - a demonstration of progressive game development with pygame.
This is aprt of a series of scripts to demonstrate the progressive development of
a simple game in python 3.7 with pygame. This script contains the classes and functions.
the main script is flappy_kenny_mods_XX
"""


__author__ = "Dr G"
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "geoff.goldrick@det.nsw.edu.au"
__status__ = "Alpha"

""" revision notes:
01 creates a 'kenny' object with a default position of 100, 100 on line 41
02 moves kenny halfway towards the mouse when game_window clicked

"""

#dependencies
import pygame as P # accesses pygame files
import sys  # to communicate with windows
from flappy_kenny_mods_02 import *  #make sure using the right one


# pygame setup - only runs once
P.init()  # starts the game engine
clock = P.time.Clock()  # creates clock to limit frames per second
loopRate = 60  # sets max speed of main loop
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 800, 600  # sets size of screen/window
game_window = P.display.set_mode(SCREENSIZE)  # creates window and game screen

# set variables for some colours if you wnat them RGB (0-255)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#create an instance of Kenny
kenny_1 = Kenny(game_window)

play = True  # controls whether to keep playing

# game loop - runs loopRate times a second!
# note:  everything in this loop is indented one tab 
while play:  # the loop runs as long as play == True

    for event in P.event.get():  # get user interaction events
        if event.type == P.QUIT:  # tests if window's X (close) has been clicked
            play = False  # causes exit of game loop
        
        # your code starts here #
        if event.type == P.MOUSEBUTTONDOWN: #includes touching screen
            # change this to do something if user clicks mouse
            # or touches screen
            kenny_1.moveTowards(event.pos)
        

    #every loop clear the screen and redraw all sprites
    game_window.fill(blue)
    kenny_1.show()
    # your code ends here #
    
    P.display.flip()  # makes any changes visible on the screen
    clock.tick(loopRate)  # limits game to frame per second, FPS value

# out of game loop #
print("Thanks for playing")  # notifies user the game has ended
P.quit()   # stops the game engine
sys.exit()  # close operating system window
