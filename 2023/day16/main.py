import re, os, functools, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from util import *
from math import gcd
from functools import *

file = open(os.path.dirname(os.path.realpath(__file__)) + '/input')
#file = open(os.path.dirname(os.path.realpath(__file__)) + '/test')

lines = file.readlines()

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

nextDir = {
    RIGHT: Pos2d(1, RIGHT),
    UP: Pos2d(0, -1),
    LEFT: Pos2d(-1, RIGHT),
    DOWN: Pos2d(0, 1),
}

beams = [(Pos2d(-1, 0), RIGHT)]

g = Grid.makeFromStrs(lines)
energized = Grid.makeUniform(g.maxRow, g.maxCol, '.')
energized.set(Pos2d(0, 0), '#')

alreadySimulated = set()

while True:
    nextBeamList = []
    for beam in beams:
        nextPos = beam[0] + nextDir[beam[1]]
        dir = beam[1]

        nextCell = g.get(nextPos)

        out1 = ()
        out2 = ()

        if nextCell == '.':
            out1 = (nextPos, dir)
        elif nextCell == '\\':
            if dir == RIGHT:
                out1 = (nextPos, DOWN)
            elif dir == UP:
                out1 = (nextPos, LEFT)
            elif dir == LEFT:
                out1 = (nextPos, UP)
            elif dir == DOWN:
                out1 = (nextPos, RIGHT)
        elif nextCell == '/':
            if dir == RIGHT:
                out1 = (nextPos, UP)
            elif dir == UP:
                out1 = (nextPos, RIGHT)
            elif dir == LEFT:
                out1 = (nextPos, DOWN)
            elif dir == DOWN:
                out1 = (nextPos, LEFT)
        elif nextCell == '|':
            if dir == UP or dir == DOWN:
                out1 = (nextPos, dir)
            else:
                out1 = (nextPos, UP)
                out2 = (nextPos, DOWN)
        elif nextCell == '-':
            if dir == RIGHT or dir == LEFT:
                out1 = (nextPos, dir)
            else:
                out1 = (nextPos, RIGHT)
                out2 = (nextPos, LEFT)

        if out1 != () and g.inBounds(out1[0]) and out1 not in alreadySimulated:
            nextBeamList.append(out1)
            energized.set(out1[0], '#')
            alreadySimulated.add(out1)
        if out2 != () and g.inBounds(out2[0]) and out2 not in alreadySimulated:
            nextBeamList.append(out2)
            energized.set(out2[0], '#')
            alreadySimulated.add(out2)

    #print(energized)
    print(energized.count('#'))
    beams = nextBeamList

print(energized)