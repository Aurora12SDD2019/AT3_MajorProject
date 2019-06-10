""" Flappy Kenny - a demonstration of progressive game development with pygame.
This is aprt of a series of scripts to demonstrate the progressive development of
a simple game in python 3.7 with pygame. This script contains the main script. The
classes and functions are in flappy_kenny_mods_XX
"""


__author__ = "Dr G"
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "geoff.goldrick@det.nsw.edu.au"
__status__ = "Alpha"

""" revision notes:
08 added a bomb class and create one instance of a bomb in bomb array
   display that bomb on right of screen at random height
07 added game over functionality
06 all movement is now done in the image reactangle for kenny
05 Added velocity and downward acceleration - see mods
04 kenny now falls at a constant rate TODO change rate to acceleration
03 adds a high score capacity. At this stage the 'score' is just number of mouse clicks
   A single score is stored a text file 'media\hi_scores.txt'
01 creates a 'kenny' object with a default position of 100, 100 on line 41
02 moves kenny halfway towards the mouse when game_window clicked line 58

"""

#dependencies
import pygame as P # accesses pygame files
import sys  # to communicate with windows
from flappy_kenny_mods_08 import *  #make sure using the right one


# pygame setup - only runs once
P.init()  # starts the game engine
clock = P.time.Clock()  # creates clock to limit frames per second
loopRate = 50  # sets max speed of main loop
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 1200, 900  # sets size of screen/window
game_window = P.display.set_mode(SCREENSIZE)  # creates window and game screen



mouse_ctr = 0

# open and read the high score files to sotre the high score
hi_score_file = open('media\hi_scores.txt', 'r')
hi_score = hi_score_file.read() #read the file
hi_score_file.close() #always good practice to close the file ASAP

#change the string values to ints
#need to use try...exzcept in case the file is empty
try:
    hi_score = int(hi_score)
except ValueError: #if the file is empty it will throw a value error
    hi_score = 0

# set variables for some colours if you want them RGB (0-255)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#create an instance of Kenny and an array to hold the bombs
bombArray = []
kenny_1 = Kenny(game_window)

play = True  # controls whether to keep playing
game_over = False

bombArray.append(Bomb(game_window))

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
            mouse_ctr += 1
     
    kenny_1.fall()
    for bomb in bombArray:
        bomb.move()
    if not game_window.get_rect().contains(kenny_1.rectangle):
        game_over = True
    
    #every loop clear the screen and redraw all sprites
    game_window.fill(blue)
    
    if game_over:
        font_over = P.font.Font(None,66)
        over_x,over_y = font_over.size("OMG - YOU KILLED KENNY!")
        game_over_text = font_over.render("OMG - YOU KILLED KENNY!",1,red, blue)
        game_window.blit(game_over_text,[(SCREENWIDTH - over_x)/2, (SCREENHEIGHT - over_y)/2])
    else:
        kenny_1.show()
    # your code ends here #
    for bomb in bombArray:
        bomb.show()

    P.display.flip()  # makes any changes visible on the screen
    clock.tick(loopRate)  # limits game to frame per second, FPS value

# out of game loop #
print("Thanks for playing")  # notifies user the game has ended
print("you pressed the mouse {} times".format(mouse_ctr))
#determine if there is a new high score
if mouse_ctr > hi_score:
    hi_score = mouse_ctr
    hi_score_file = open('media\hi_scores.txt', 'w')
    hi_score_file.write("{}".format(hi_score))
    hi_score_file.close()
    print("the new high score is {}".format(hi_score))

P.quit()   # stops the game engine
sys.exit()  # close operating system window
