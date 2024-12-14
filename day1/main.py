import re, os, functools, sys

sys.path.insert(0, '..')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from util import *

file = open(os.path.dirname(os.path.realpath(__file__)) + '/input')
lines = file.readlines()

lefts = []
rights = []

for line in lines:
    nums = re.search(r'(\d*) *(\d*)', line).groups()
    lefts.append(int(nums[0]))
    rights.append(int(nums[1]))

lefts = sorted(lefts)
rights = sorted(rights)

sums = sum([abs(i - j) for i, j in zip(lefts, rights)])
print(sums)

score = sum([rights.count(i) * i for i in lefts])

print(score)