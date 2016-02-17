from levelio import *
from state import *
from world import *

def runMain():
    state = GameState(openLevel("./levels/tut.txt"))

    state.draw()
    state.movePlayer(0)
    state.draw()
    state.movePlayer(1)
    state.draw()
    state.movePlayer(2)
    state.draw()
    state.movePlayer(3)
    state.draw()
