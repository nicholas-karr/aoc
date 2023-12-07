import re, os, functools, sys
from collections import defaultdict
    
def extractNums(string):
    nums = []

    match = re.findall(r'(\d+)', string)
    for i in match:
        nums.append(int(i))

    return nums

# [lmin, lmax] on [rmin, rmax]
def overlaps(lmin, lmax, rmin, rmax):
    if lmin > lmax or rmin > rmax:
        return False

    return lmax >= rmin and lmin <= rmax

def isIn(val, min, max):
    return val >= min and val <= max

def getOverlap(lmin, lmax, rmin, rmax):
    begin = 0
    end = 0

    begin = max(lmin, rmin)
    end = min(lmax, rmax)

    return (begin, end)

def beats(ms, dist, newMs):
    travelTime = ms - newMs
    travelled = (ms - newMs) * newMs
    return travelled > dist

def getBounds(ms, dist):
    a = 1
    b = -ms
    c = dist

    u = (-b + pow(b * b - 4 * a * c, .5)) // 2 * a 
    d = (-b - pow(b * b - 4 * a * c, .5)) // 2 * a 

    return u - d

file = open(os.path.dirname(os.path.realpath(__file__)) + '/input')
lines = file.readlines()

times = extractNums(lines[0])
distances = extractNums(lines[1])

races = list(zip(times, distances))

cnt = 1

for time, dist in races:
    cnt *= getBounds(time, dist)


print(cnt)