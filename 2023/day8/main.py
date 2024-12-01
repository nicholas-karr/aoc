import re, os, functools, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from util import *
from math import gcd
from functools import *


file = open(os.path.dirname(os.path.realpath(__file__)) + '/input')
lines = file.readlines()

HERE = 'AAA'
GOAL = 'ZZZ'

elmsList = lines[2:]
elms = {}


for i in elmsList:
    name = i.split(' ')[0]
    m = re.findall(r'(\w\w\w)', i)
    tup = (m[0], m[1], m[2])
    elms[name] = tup

pathOrig = clean(lines[0])
path = pathOrig

starts = [i for i in elms.values() if i[0][2] == 'A']
ends = [i for i in elms.values() if i[0][2] == 'Z']

stepCnt = 0

def isAllEnds(l1):
    for i in l1:
        if i[2] != 'Z':
            return False
        
    return True

# starting space to length of cycle to end space
cycle = {}
spaceCycles = {}

for start in starts:
    node = start

    while node[0][2] != 'Z':
        dir = node[1 if path[0] == 'L' else 2]
        node = elms[dir]

        stepCnt += 1
        path = path[1:]
        if len(path) == 0:
            path = pathOrig

    cycle[start] = node
    spaceCycles[start] = stepCnt

    stepCnt = 0
    path = pathOrig

print(spaceCycles.values())
print(reduce(gcd, tuple(spaceCycles.values())))

while not isAllEnds(i):
    nextList = []

    for index, j in enumerate(i):
        dir = j[1 if path[0] == 'L' else 2]
        i[index] = elms[dir]

    stepCnt += 1

    path = path[1:]
    if len(path) == 0:
        path = pathOrig


print(stepCnt)