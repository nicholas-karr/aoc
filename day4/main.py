import re, os, functools, sys

sys.path.insert(0, '..')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from util import *

file = open(os.path.dirname(os.path.realpath(__file__)) + '/input')
lines = file.readlines()

grid = Grid.makeFromStrs(lines)

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

def hasStr(x, y, s):
    def check(pos, c):
        return grid.get(pos) == c
    
    if not check(Pos2d(x, y), s[0]):
        return 0
    
    has = 0
    
    for dir in dirs:
        pos = Pos2d(x, y)
        got = 0
        for i in range(len(s)):
            if check(pos, s[i]):
                got += 1
            
            pos = Pos2d(pos.x + dir[0], pos.y + dir[1])

        if got == len(s):
            has += 1

    return has

'''cnt = 0
for x in range(grid.maxCol):
    for y in range(grid.maxRow):
        cnt += hasStr(x, y, 'XMAS')

print(grid)
print(cnt)
'''

cnt = 0
for x in range(grid.maxCol):
    for y in range(grid.maxRow):
        pos = Pos2d(x, y)
        if grid.get(pos) != 'A':
            continue

        g = [grid.get(Pos2d(pos.x - 1, pos.y + 1)), grid.get(Pos2d(pos.x + 1, pos.y - 1))]

        if sorted([grid.get(Pos2d(pos.x - 1, pos.y + 1)), grid.get(Pos2d(pos.x + 1, pos.y - 1))]) == ['M', 'S']:
            if sorted([grid.get(Pos2d(pos.x + 1, pos.y + 1)), grid.get(Pos2d(pos.x - 1, pos.y - 1))]) == ['M', 'S']:
                cnt += 1


print(cnt)