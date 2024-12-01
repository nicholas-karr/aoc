import re, os, functools, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from util import *
from math import gcd
from functools import *

file = open(os.path.dirname(os.path.realpath(__file__)) + '/input')
#file = open(os.path.dirname(os.path.realpath(__file__)) + '/test')

lines = file.readlines()

class Lens:
    def __init__(self, label):
        self.label = label

def hash(s):
    v = 0
    for i in s:
        code = ord(i)
        v += code
        v *= 17
        v %= 256

    return v

boxes = [[] for i in range(256)]

def op(s):
    (label, command, *length) = re.findall(r'(\w*)(=|-)(\d*)', s)[0]
    
    lens = Lens(label)
    h = hash(label)
    box = boxes[h]
    print(length)

    if command == '=':
        lens.length = int(length[0])

        for index, i in enumerate(box):
            if label == i.label:
                box[index] = lens
                break

        if label not in [i.label for i in box]:
            box.append(lens)

    else:
        for index, i in enumerate(box):
            if label == i.label:
                del box[index]
                break


ins = lines[0].split(',')

#print(ins)

vals = [hash(i) for i in ins]

#print(vals)
print(sum(vals))



for i in ins:
    op(i)

powers = []
for index, box in enumerate(boxes):
    for slot, lens in enumerate(box):
        p = (index + 1) * (slot + 1) * lens.length
        powers.append(p)

print(powers)
print(sum(powers))