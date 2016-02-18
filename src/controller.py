import time

# Two usages of the game controlling class:
# 1. Initialize, then call the interactive loop.
# 2. Don't initialize, instead run unittestController.

from levelio import *
from state import *

class Controller:
    def __init__(self, filename):
        self._state = GameState(openLevel(filename))

    def interactiveLoop(self):
        self._drawWorld()
        while True:
            chars = self._waitForKeyboardInput()
            if chars == 'q':
                break
            try:
                direc = {'i' : 0, 'o' : 1, 'e' : 2, 'n' : 3}[chars]
                self._state.movePlayer(direc)
            except KeyError:
                pass
            self._drawWorld()
            if self._state.done():
                print "You have collected all diamonds! You win!"
                break

    def _drawWorld(self):
        for _ in range(self._state.world().yl(), 25):
            print # clear screen by shifting the previous drawing away
        self._state.draw()

    def _waitForKeyboardInput(self):
        print "Diamonds '.' left to collect: %d" \
            % self._state.world().diamondsLeft()
        print "Move around with [n], [e], [i], [o], or [q] to quit."
        return raw_input("> ")

def unittestController():
    ctrl = Controller("./levels/tut.txt")

    def move(direc):
        ctrl._state.movePlayer(direc)
        time.sleep(0.5)
        ctrl._drawWorld()

    for direc in [0, 3, 3, 3, 3, 1, 2, 2, 3, 3, 3, 3, 3]:
        move(direc)
