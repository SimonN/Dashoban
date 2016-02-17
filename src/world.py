class World:
    def __init__(self, xl, yl):
        self.xl = xl
        self.yl = yl
        self.arr = []

    def get(self, x, y):
        if 0 <= x < self.xl and 0 <= y < self.yl:
            return self.arr[y][x]
        else:
            return '#'

    def set(self, x, y, char):
        assert 0 <= x < self.xl and 0 <= y < self.yl
        arr[y][x] = char

    def draw(self):
        for line in self.arr:
            print line
