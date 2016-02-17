# Today I learned: Python's member naming convention is like D's:
# Private members are prefixed with _. Only that these members aren't
# private, and aren't made private through the underscore. >_>

import sys

class World:
    def __init__(self, xl, yl, arrOfString):
        self._xl  = xl
        self._yl  = yl
        self._arr = self._arrayOfArrayOfChar(arrOfString)

    # The world can be legally queried at any coordinate, even outside
    def get(self, x, y):
        if 0 <= x < self._xl and 0 <= y < self._yl:
            return self._arr[y][x]
        else:
            return '#'

    def set(self, x, y, char):
        assert self.get(x, y) != '#'
        self._arr[y][x] = char

    def findPlayer(self):
        ret = []
        for y in range(0, self._yl):
            for x in range(0, self._xl):
                if (self.get(x, y) == '@'):
                    assert ret == [], """can't have >= 1 player '@' in level.
                        Found one at %d,%d, another now at %d,%d.
                        """ % (ret[0], ret[1], x, y)
                    ret = [x, y]
        assert ret != [], "the level lacks a player starting point '@'"
        return ret

    def draw(self):
        for line in self._arr:
            for char in line:
                sys.stdout.write(char)
            print #newline

    # Input array holds longer strings.
    # Output array is rectangular, holds arrays of one-char strings
    def _arrayOfArrayOfChar(self, arrOfString):
        assert self._xl > 0
        assert self._yl > 0
        arr = []
        for y in range(0, self._yl):
            arr += [[]]
            for x in range(0, self._xl):
                try:
                    arr[y] += arrOfString[y][x]
                except IndexError:
                    arr[y] += ' '
            assert len(arr[y]) == self._xl
        assert len(arr) == self._yl
        return arr
