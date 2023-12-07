class Grid:
    def __init__(self, arr, maxRow, maxCol):
        self.arr = arr
        self.maxRow = maxRow
        self.maxCol = maxCol

    def inBounds(self, row, col):
        return row >= 0 and row < self.maxRow and col >= 0 and col < self.maxCol
    
    def get(self, row, col, default = 0):
        if not self.inBounds(row, col):
            return default
        else:
            return self.arr[row][col]
        
    def getCol(self, col):
        return [i[col] for i in self.arr]
    
    def getRow(self, row):
        return self.arr[row]