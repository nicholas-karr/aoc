import re, os, functools, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from util import *
from math import gcd
from functools import *

file = open(os.path.dirname(os.path.realpath(__file__)) + '/input')

#file = open(os.path.dirname(os.path.realpath(__file__)) + '/test')

#file = open(os.path.dirname(os.path.realpath(__file__)) + '/input2')

lines = file.readlines()

g = Grid.makeFromStrs(lines)

goal = g.indexOf('S')
#goalNext = Pos2d(goal.x + 1, goal.y)

dirOffsets = {
    'n': Pos2d(0, -1),
    'e': Pos2d(1, 0),
    's': Pos2d(0, 1),
    'w': Pos2d(-1, 0)
}

shapeConnects = {
    '|': [ dirOffsets['n'], dirOffsets['s'] ],
    '-': [ dirOffsets['e'], dirOffsets['w'] ],
    'L': [ dirOffsets['n'], dirOffsets['e'] ],
    'J': [ dirOffsets['n'], dirOffsets['w'] ],
    '7': [ dirOffsets['w'], dirOffsets['s'] ],
    'F': [ dirOffsets['e'], dirOffsets['s'] ],
    'S': [ dirOffsets['n'], dirOffsets['e'], dirOffsets['s'], dirOffsets['w'],  ],
    '.': [],
}

def hasConnectionTowards(p1, p2, p1Shape):
    for i in p1Shape:
        potential = p1 + i
        if potential == p2:
            return True
        
    return False

# 2 nodes connect when their theoretical connections contain each other
def connects(p1, p2):
    if not g.inBounds(p1) or not g.inBounds(p2):
        return False

    p1Shape = shapeConnects[g.get(p1)]
    p2Shape = shapeConnects[g.get(p2)]

    return hasConnectionTowards(p1, p2, p1Shape) and hasConnectionTowards(p2, p1, p2Shape)

def findNext(pos, prev):
    for i in dirOffsets.values():
        if pos + i != prev:
            test = pos + i
            if connects(test, pos):
                return test
            
    raise None

#s = connects(Pos2d(1, 1), Pos2d(1, 2))

goalConnectsTo = []
for i in dirOffsets.values():
    test = goal + i
    if connects(test, goal):
        goalConnectsTo.append(test)

goalIs = [i for i, j in shapeConnects.items() if j == goalConnectsTo]

goalNext = goalConnectsTo[0]

path = [goalNext]

prevPos = goal
pos = goalNext
while pos != goal:
    # go in the direction that isn't towards prevPos
    nextPos = findNext(pos, prevPos)
    prevPos = pos
    pos = nextPos

    path.append(pos)

print(path)

#pathLength = len(path) / 2
#print(pathLength)

image = Grid.makeUniform(g.maxRow, g.maxCol, '.')

for i in path:
    image.set(i, 'X')

def touchingOutside(pt):
    return pt.x == 0 or pt.x == image.maxCol - 1 or pt.y == 0 or pt.y == image.maxRow - 1

def isEnclosed(pt):
    if image.get(pt) == 'X':
        raise Exception
        pass
    
    #line = ''.join([g.arr[pt.y][i] for i in range(g.maxCol - pt.x) if image.arr[pt.y][i] == 'X'])
    #line = ''.join([g.arr[pt.y][i] for i in range(g.maxCol - pt.x) if image.arr[pt.y][i] == 'X'])
    #line = g.arr[pt.y][pt.x + 1:]

    line = ''
    con = 0

    for x in range(g.maxCol):
        if x <= pt.x:
            continue
        if image.arr[pt.y][x] == 'X':
            line += g.arr[pt.y][x]

    prevLine = ''

    for x in range(g.maxCol):
        if x >= pt.x:
            continue
        if image.arr[pt.y][x] == 'X':
            prevLine += g.arr[pt.y][x]

            if prevLine[-1] in ['|', 'J', 'L']:
                con += 1

    if line == 'FJLJ':
        pass

    #regex = r'(?:F|L)-*(?:J|7)|\|'
    regex = r'J|L|\|'

    prevLine = g.arr[pt.y][:pt.x]

    match = re.findall(regex, line)
    prevMatch = re.findall(regex, prevLine)
    cnt = len(match)
    cnt2 = len(prevMatch)

    #cnt = cnt + cnt2

    #if cnt % 2 == 1 and cnt2 % 2 == 1:
    #    return True

    if touchingOutside(pt):
        return False

    #return False
    return con % 2 == 1

# Color every . as either in the region (+) or outside it (-)

path = set(path)

for row in range(g.maxRow):
    for col in range(g.maxCol):
        val = g.get(Pos2d(col, row))

        pos = Pos2d(col, row)

        if pos in path:
            continue

        enc = isEnclosed(pos)

        if enc:
            image.set(pos, '+')
        else:
            image.set(pos, '-')

print(g)
print(image)
print(len([j for i in image.arr for j in i if j == '+']))