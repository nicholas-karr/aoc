import re, os, functools, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from util import *
from math import gcd
from functools import *


file = open(os.path.dirname(os.path.realpath(__file__)) + '/input')
lines = file.readlines()

seqs = [extractNums(i) for i in lines]
s = 0
for line in seqs:

    differences = [line]
    
    newSeq = line

    while not all(v == 0 for v in newSeq):
        nextSeq = []

        for i, val in list(enumerate(newSeq))[1:]:
            dif = newSeq[i] - newSeq[i - 1]
            nextSeq.append(dif)

        newSeq = nextSeq

        differences.append(nextSeq)

    differences[-1].insert(0, 0)

    for i in reversed(range(len(differences) - 1)):
        differences[i].insert(0, differences[i][0] - differences[i + 1][0])

    s += differences[0][0]
    
print(s)