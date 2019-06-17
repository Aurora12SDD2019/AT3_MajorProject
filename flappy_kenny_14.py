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
14: add testing of input names against banned list
13 added leader board class to store best scores and names.
   Changed gameover loop to display leader board
12 add scores to game over screen lines 104+
   add red screen to end on game if hit by bomb
   kenny image changes to dead image lines 120 and 130
11 adds a "killed kenny" sound at end of game. Adds explosion if kenny killed by bomb.
10 lines 105 + check to see if any of the bombs hit kenny and then end the game
   lines 116+ removes bombs that go off left of screen from array and increase the score
09 added bombs according to a rate defined by bomb_rate on line 42.
   The bombs are added on lines 100 to 103
   Score now depends on how many bombs added line 104
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
from flappy_kenny_mods_14 import *  #make sure using the right one


# pygame setup - only runs once
P.init()  # starts the game engine
clock = P.time.Clock()  # creates clock to limit frames per second
loopRate = 50  # sets max speed of main loop
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 1200, 900  # sets size of screen/window
game_window = P.display.set_mode(SCREENSIZE)  # creates window and game screen
bomb_array = []
bomb_rate = 1500  # time in millisecs between adding bombs
bomb_last_added = 0 #last time a bomb was added to the cup_array
kenny = Kenny(game_window)
# background_muzak = P.mixer.Sound('sound/jungle_run_01.ogg')
game_over_sound = P.mixer.Sound('media/explosion.wav')
killed_kenny_sound = P.mixer.Sound('media/killed_kenny.ogg')

score = 0

leader_board = LeaderBoard()

# set variables for some colours if you want them RGB (0-255)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


play = True  # controls whether to keep playing
game_over = False
score_checked = False


# game loop - runs loopRate times a second!
# note:  everything in this loop is indented one tab 
while play:  # the loop runs as long as play == True
    now = P.time.get_ticks() #get the time since program started in millisecs

    for event in P.event.get():  # get user interaction events
        if event.type == P.QUIT:  # tests if window's X (close) has been clicked
            play = False  # causes exit of game loop
        
        # your code starts here #
        if event.type == P.MOUSEBUTTONDOWN: #includes touching screen
            # change this to do something if user clicks mouse
            # or touches screen
            kenny.moveTowards(event.pos)
     

    
    #every loop clear the screen and redraw all sprites
    game_window.fill(blue)
    
    if game_over:       
        y_offset = -350
        font_over = P.font.Font(None,60)
        score_x,score_y = font_over.size("Your score: {}".format(score))        
        score_text = font_over.render("Your score: {}".format(score),1,red, blue)
        game_window.blit(score_text,[(SCREENWIDTH - score_x)/2, y_offset+(SCREENHEIGHT - score_y)/2])
        
        if not score_checked:
            if leader_board.check(score) == True:
                print("WINNER! WINNER! CHICKEN DINNER")
                leader_board.update(score)
            score_checked = True
        
        font_over = P.font.Font(None,40)
        y_offset += 100
        for l in leader_board.leaders:
            score_x,score_y = font_over.size("{}   {}".format(l[1], l[0]))        
            score_text = font_over.render("{}   {}".format(l[1], l[0]),1,red, blue)
            game_window.blit(score_text,[(SCREENWIDTH - score_x)/2, y_offset+(SCREENHEIGHT - score_y)/2])
            y_offset += 50
            
        final_screen = True

            
    else:
        kenny.fall()
    
        if not game_window.get_rect().contains(kenny.rectangle):
            game_over = True
            killed_kenny_sound.play()
            kenny.image = P.image.load("media/kenny_dead.png")

        for bomb in bomb_array:
            bomb.move()
            bomb.show()
            # check to see if kenny hit
            if bomb.rectangle.colliderect(kenny.rectangle):
                game_over = True
                game_over_sound.play()
                killed_kenny_sound.play()
                kenny.image = P.image.load("media/kenny_dead.png")
                game_window.fill(red)
                P.display.flip()
                P.time.wait(300)


            
            #check to see if off the screen
            if bomb.rectangle.x < -bomb.rectangle.width:
                bomb_array.remove(bomb)
                score += 1

        #see if it is time to add a bomb
        if (now - bomb_last_added > bomb_rate): #time to add a bomb
            bomb_array.append(Bomb(game_window))
            bomb_last_added = now
            bomb_rate -= 3
            print("{} bombs in play".format(len(bomb_array)))
    
    kenny.show()

# your code ends here #

    P.display.flip()  # makes any changes visible on the screen
    clock.tick(loopRate)  # limits game to frame per second, FPS value

# out of game loop #
print("Thanks for playing")  # notifies user the game has ended
#print("the current high score is {}".format(hi_score))
print("your score was {}".format(score))


    
P.quit()   # stops the game engine
sys.exit()  # close operating system window
