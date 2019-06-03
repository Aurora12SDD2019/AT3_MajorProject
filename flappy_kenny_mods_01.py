""" Flappy Kenny - a demonstration of progressive game development with pygame.
This is aprt of a series of scripts to demonstrate the progressive development of
a simple game in python 3.7 with pygame. This script contains the classes and functions.
the main script is flappy_kenny_XX
"""

__author__ = "Dr G"
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "geoff.goldrick@det.nsw.edu.au"
__status__ = "Alpha"


""" revision notes:
01: sets up the basic kenny class. The important stiff is done in the
    __init__ function which sets up the default values of the object,
    and the show function which places it on the screen.
    

"""

#import statements for any dependencies
import pygame as P
import random as R

#modules - write your modules here using the templates below

class Kenny(object):
    """Creates and renders a Kenny object.

    renders the keny image and blits it to the playing screen at position 100, 100

    Attributes:
        image: the image of kenny.
        position: An integer array with the x and y coordinates of theimage
        window: the playing window
    """

    def __init__(self, window):
        """Inits SampleClass with blah.
        
        Args:
            window: a pygame.display object to display kenny on
        """
        self.window = window
        self.position = [100, 100]
        self.image = P.image.load("media\kenny.gif").convert() #render the image
        self.show()


    def show(self):
        self.window.blit(self.image, self.position) #put the image on the window



# templates copy and paste these for your own function and class definitions
def function_name(arg1, arg2, other_silly_variable=None):
    """Does something amazing.

    a much longer description of the really amazing stuff this function does and how it does it.

    Args:
        arg1: the first argument required by the function.
        arg2: the second argument required by the function.
        other_silly_variable: Another optional variable, that has a much
            longer name than the other args, and which does nothing.

    Returns:
        description of the stuff that is returned by the function.

    Raises:
        AnError: An error occurred running this function.
    """
    pass



class SampleClass(object):
    """Summary of class here.

    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam=False):
        """Inits SampleClass with blah."""
        self.likes_spam = likes_spam
        self.eggs = 0

    def public_method(self):
        """Performs operation blah."""



