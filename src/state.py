

class GameState:
    def __init__(self, world):
        self._world = world
        self._playerX = self._world.findPlayer()[0]
        self._playerY = self._world.findPlayer()[1]
        self._done    = False

    def done(self):
        return self._done

    def movePlayer(self, direc):
        assert direc >= 0 and direc < 4
        assert self._world.get(self._playerX, self._playerY) == '@'
        plusX  = [0, 1, 0, -1][direc]
        plusY  = [-1, 0, 1, 0][direc]
        onto   = self._world.get(self._playerX + plusX,
                                 self._playerY + plusY)
        behind = self._world.get(self._playerX + 2 * plusX,
                                 self._playerY + 2 * plusY)
        if onto == ' ':
            self._movePlayerLeaveSpace(plusX, plusY)
        elif onto == '.':
            self._collectDiamond(plusX, plusY)
        elif onto in ['+', '-', '|'] and behind == ' ':
            self._pushCrate(plusX, plusY)

    def draw(self):
        self._world.draw()

    def _movePlayerLeaveSpace(self, plusX, plusY):
        self._world.set(self._playerX, self._playerY, ' ')
        self._playerX += plusX
        self._playerY += plusY
        self._world.set(self._playerX, self._playerY, '@')

    def _collectDiamond(self, plusX, plusY):
        self._movePlayerLeaveSpace(plusX, plusY)
        if self._world.diamondsLeft == 0:
            _done = True

    def _pushCrate(self, plusX, plusY):
        char = self._world.get(self._playerX + plusX,
                               self._playerY + plusY)
        self._world.set(self._playerX + 2 * plusX,
                        self._playerY + 2 * plusY, char)
        self._movePlayerLeaveSpace(plusX, plusY)
