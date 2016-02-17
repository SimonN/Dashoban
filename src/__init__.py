from world import *
from levelio import *

def runMain():
    world = openLevel("./levels/tut.txt")
    world.draw();
