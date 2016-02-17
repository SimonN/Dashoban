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
            return self.arr[y][x]
        else:
            return '#'

    def set(self, x, y, char):
        assert get(self, x, y) != '#'
        arr[y][x] = char

    def draw(self):
        for line in self._arr:
            for char in line:
                sys.stdout.write(char)
            print #newline

    def _arrayOfArrayOfChar(self, inputArr):
        assert self._xl > 0
        assert self._yl > 0
        arr = []
        for y in range(0, self._yl):
            arr += [[]]
            for x in range(0, self._xl):
                try:
                    arr[y] += inputArr[y][x]
                except IndexError:
                    arr[y] += ' '
            assert len(arr[y]) == self._xl
        assert len(arr) == self._yl
        return arr
