from operator import itemgetter

class Pos2d():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    """(tuple)
    __slots__ = []

    def __new__(self, x, y):
        return tuple.__new__(self, (x, y))
    
    x = property(itemgetter(0))
    y = property(itemgetter(1))

    @property
    def x(self):
        return tuple.__getitem__(self, 0)
    
    @property
    def y(self):
        return tuple.__getitem__(self, 1)
    """

    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
    
    def __add__(self, rhs):
        return Pos2d(self.x + rhs.x, self.y + rhs.y)
    
    def __sub__(self, rhs):
        return Pos2d(self.x - rhs.x, self.y - rhs.y)
    
    def __eq__(self, rhs):
        return self.x == rhs.x and self.y == rhs.y
    
    def __getitem__(self, item):
        raise TypeError
    
    def __hash__ (self):
        return self.x.__hash__() ^ self.y.__hash__()
    
    def get(self):
        return Pos2d(self.x, self.y)

class Grid:
    def __init__(self, maxRow, maxCol, arr = None):
        self.arr = arr
        self.maxRow = maxRow
        self.maxCol = maxCol

    def inBounds(self, pos):
        row = pos.y
        col = pos.x
        return row >= 0 and row < self.maxRow and col >= 0 and col < self.maxCol
    
    def get(self, pos, default = 0):
        if not self.inBounds(pos):
            if default is not None:
                return default
            else:
                raise Exception
        else:
            return self.arr[pos.y][pos.x]
        
    def set(self, pos, val):
        if not self.inBounds(pos):
            raise Exception
        else:
            self.arr[pos.y][pos.x] = val
        
    def getCol(self, col):
        return [i[col] for i in self.arr]
    
    def getRow(self, row):
        return self.arr[row]
    
    def indexOf(self, target):
        for row in range(self.maxRow):
            for col in range(self.maxCol):
                pos = Pos2d(col, row)

                if self.get(pos, None) == target:
                    return pos
                
    def __iter__(self):
        self.i = 0
        return self
    
    def __next__(self):
        col = self.i % self.maxCol
        row = (self.i - col) // self.maxCol
        pos = Pos2d(col, row)

        self.i += 1

        if not self.inBounds(pos):
            raise StopIteration

        return (pos, self.get(pos, None))

    def makeUniform(maxRow, maxCol, val):
        s = Grid(maxRow, maxCol)

        row = [val] * maxCol

        s.arr = []
        for i in range(maxRow):
            s.arr.append(row[:])

        s.maxRow = maxRow
        s.maxCol = maxCol

        return s
    
    def makeFromStrs(lines):
        lines = [i.strip() for i in lines]
        g = Grid(len(lines), len(lines[0]), lines)
        return g

    def __str__(self):
        s = ''

        # assume output width of 0
        for row in range(self.maxRow):
            for col in range(self.maxCol):
                pos = Pos2d(col, row)
                val = self.get(pos)

                s += val

            s += '\n'

        return s