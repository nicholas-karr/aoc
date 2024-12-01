import re, os, functools, sys
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
    
def extractNums(string):
    nums = []

    match = re.findall(r'(\d+)', string)
    for i in match:
        nums.append(int(i))

    return nums

file = open(os.path.dirname(os.path.realpath(__file__)) + '/input')
lines = file.readlines()

scores = []
evals = 0
matches = {} # card num -> scratch cards produced by card

def procGame(row, line):
    global evals
    evals += 1

    match = re.search(r'Card[ \d]+: ([\d ]+) \| ([\d ]+)', line)
    g = match.groups()
    (winning, have) = match.groups()

    winning = extractNums(winning)
    have = extractNums(have)

    score = 0

    for i in have:
        if i in winning:
            if score == 0:
                score = 1
            else:
                #score *= 2
                score += 1

    #scores.append(score)

    totalScore = score

    for i in range(score):
        totalScore += matches[row + i + 1]

    matches[row] = totalScore

    evals += totalScore

#for row, line in enumerate(lines):
#    procGame(row, line)

for row, line in reversed(list(enumerate(lines))):
    procGame(row, line)

print(sum(scores))
print(evals)