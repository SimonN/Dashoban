from levelio import *
from state import *
from world import *

def runMain():
    state = GameState(openLevel("./levels/tut.txt"))
