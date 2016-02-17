

class GameState:
    def __init__(self, world):
        self._world = world
        self._playerX = world.findPlayer()[0]
        self._playerY = world.findPlayer()[1]
        world.draw()
        print "player is at %d,%d" % (self._playerX, self._playerY)
