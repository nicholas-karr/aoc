import re, os, functools, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from util import *
from math import gcd
from functools import *

file = open(os.path.dirname(os.path.realpath(__file__)) + '/input')
#file = open(os.path.dirname(os.path.realpath(__file__)) + '/test')

lines = file.readlines()

g = Grid.makeFromStrs(lines)
#g.replace('', '.')

print(g)

for row in range(g.maxRow):
    for col in range(g.maxCol):
        if g.get(Pos2d(col, row)) == 'O':
            g.set(Pos2d(col, row), '.')

            height = row
            while height > 0 and g.get(Pos2d(col, height - 1)) == '.':
                height -= 1

            g.set(Pos2d(col, height), 'O')

print(g)

total = 0
for row in range(g.maxRow):
    for col in range(g.maxCol):
        if g.get(Pos2d(col, row)) == 'O':
            height = row
            spaces = 1
            while height < g.maxRow - 1 and g.get(Pos2d(col, height + 1)) != '':
                spaces += 1
                height += 1

            total += spaces
    
print(total)