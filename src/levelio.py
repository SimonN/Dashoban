from world import *

def openLevel(filename):
    xl = 0
    yl = 0
    charArr = []
    myFile = open(filename, 'r')

    for line in myFile:
        xl = max(xl, len(line.strip()))
        charArr += [line.strip()]
        yl += 1
    world = World(xl, yl, charArr)
    return world
