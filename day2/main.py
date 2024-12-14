import re, os, functools, sys

sys.path.insert(0, '..')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from util import *

file = open(os.path.dirname(os.path.realpath(__file__)) + '/input')
lines = file.readlines()

safe = 0

def isSafe(num, prev, decr):
    if num > prev and decr:
        return False
    if num < prev and not decr:
        return False
    if num == prev:
        return False
    if abs(num - prev) > 3:
        return False
    
    return True

for line in lines:
    prev = int(line.split()[0]) - 1
    notSafe = False

    nums = [int(i) for i in line.split()]
    decr = False
    if nums[0] > nums[1]:
        prev += 2
        decr = True

    for num in nums:
        if not isSafe(num, prev, decr):
            notSafe = True
        prev = num

    nowSafe = False
    if notSafe:
        for numToRemove in range(len(nums)):
            cpy = nums.copy()
            del cpy[numToRemove]
            prev = cpy[0] - 1
            if cpy[0] > cpy[1]:
                prev += 2
                decr = True
            else:
                decr = False
            notSafe = False

            for num in cpy:
                if not isSafe(num, prev, decr):
                    notSafe = True
                prev = num

            if not notSafe:
                nowSafe = True

    if nowSafe or not notSafe:
        safe += 1

print(safe)