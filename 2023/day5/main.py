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


class Mapper():
    def __init__(self):
        self.ranges = []
    
    def __getitem__(self, i):
        for rMin, rMax, offset in self.ranges:
            if i >= rMin and i <= rMax:
                return i + offset - rMin
            
        pass

def procMap(line):
    mapName = re.search(r'(\w+)( map)?:', line)[1]

    maps = line.splitlines()[1:]

    mapper = Mapper()

    for m in maps:
        (destStart, srcStart, cnt) = extractNums(m)

        mapper.ranges.append((srcStart, srcStart + cnt - 1, destStart))

    return mapper
    


file = open(os.path.dirname(os.path.realpath(__file__)) + '/input')
lines = file.readlines()

megaLine = ''.join(lines)

maps = megaLine.split('\n\n')

seeds = extractNums(maps[0])

bundles = list(zip(seeds[::2], seeds[1::2]))
#bundles = [(i, i) for i in seeds]
#bundles = [(79, 79)]
bundles = [(i, i + j - 1) for (i, j) in bundles]
#bundles = [(i, i) for (i, j) in bundles]



for m in maps[1:]:
    dict = procMap(m)
    newBundles = []

    for start, end in bundles:
        overlapped = False
        for rMin, rMax, destStart in dict.ranges:
            # [4, 6] on [5, 7] -> [5, 6]
            if overlaps(start, end, rMin, rMax):
                overlapped = True
                newRange = getOverlap(start, end, rMin, rMax)

                lower = (start, rMin)
                upper = (rMax, end)

                #if lower[0] < lower[1]:
                    #newBundles.append(lower)
                #if upper[0] < upper[1]:
                    #newBundles.append(upper)

                newRangeOut = (newRange[0] - rMin + destStart, newRange[1] - rMin + destStart - 1)

                #if newRangeOut[0] < newRangeOut[1]:
                newBundles.append(newRangeOut)

                if min([i for i, j in newBundles]) == 0:
                    pass

        if not overlapped:
            newBundles.append((start, end))
            if min([i for i, j in newBundles]) == 0:
                pass

    bundles = newBundles

bundles = [(i, j) for i, j in bundles if i != 0]
print(min([i for i, j in bundles]))