import re, os, functools

surrounding = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]

file = open(os.path.dirname(os.path.realpath(__file__)) + '/input')
lines = file.readlines()

lines = [i[:-1] for i in lines]

linecnt = len(lines) - 1
linelen = len(lines[0]) - 1

parts = []

# pos tuple to part num
parts = {}

def getAt(row, col, maxRow, maxCol, arr, default):
    if row < 0 or row >= maxRow or col < 0 or col >= maxCol:
        return default
    else:
        return arr[row][col]

def hasSurroundingSpecial(row, col):
    def match(row, col):
        res = getAt(row, col, linecnt, linelen, lines, '.')
        return not res.isnumeric() and res != '.'

    res = [match(row + i, col + j) for (i, j) in surrounding]

    return sum(res) != 0
    

def readParts(row):
    global parts

    string = lines[row]
    num = ''
    keep = False

    for i, c in enumerate(string + '.'):
        if c.isnumeric():
            num = num + c
        else:
            if keep:
                for j, c2 in enumerate(num):
                    parts[(row, i - j - 1)] = int(num)

                num = ''
                keep = False
            else:
                num = ''
        
        if hasSurroundingSpecial(row, i) and c.isnumeric():
            keep = True


for i in range(len(lines)):
    readParts(i)

gearRatios = []

for row in range(len(lines)):
    for col in range(linelen + 1):
        if getAt(row, col, linecnt, linelen, lines, '.') == '*':
            ratios = []

            for (i, j) in surrounding:
                pos = (i + row, j + col)
                if pos in parts:
                    ratios.append(parts[pos])

            ratios = list(set(ratios))

            if len(ratios) == 2:
                gearRatios.append(ratios[0] * ratios[1])


print(len(parts))

s = sum(gearRatios)

print(s)