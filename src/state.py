

class GameState:
    def __init__(self, world):
        self._world = world
        self._playerX = self._world.findPlayer()[0]
        self._playerY = self._world.findPlayer()[1]
        self._world.draw()
        print "player is at %d,%d" % (self._playerX, self._playerY)
        self.movePlayer(0)
        self.movePlayer(1)
        self.movePlayer(2)
        self.movePlayer(3)

    def movePlayer(self, direc):
        assert direc >= 0 and direc < 4;
        assert self._world.get(self._playerX, self._playerY) == '@'
        plusX  = [0, 1, 0, -1][direc]
        plusY  = [-1, 0, 1, 0][direc]
        onto   = self._world.get(self._playerX +   plusX,
                                 self._playerY +   plusY)
        behind = self._world.get(self._playerX + 2*plusX,
                                 self._playerY + 2*plusY)
