from controller import *
from levelio import *
from state import *
from world import *

def runMain():
    print "Dashoban"
    print "Press [Enter] to play the tutorial."
    print "Alternatively, enter a filename, e.g. `levels/simon01.txt'."
    filename = raw_input("> ")
    if not filename:
        filename = "levels/tut.txt"
    try:
        ctrl = Controller(filename)
        ctrl.interactiveLoop()
    except IOError:
        print "File `" + filename + "' doesn't exist. Aborting."
