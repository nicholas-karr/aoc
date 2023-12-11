import re

from util.grid import *
from util.sort import *

def clean(s):
    return s.strip()

def extractNums(string):
    nums = []

    match = re.findall(r'(-?\d+)', string)
    for i in match:
        nums.append(int(i))

    return nums