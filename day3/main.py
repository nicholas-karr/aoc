import re, os, functools, sys

sys.path.insert(0, '..')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from util import *

file = open(os.path.dirname(os.path.realpath(__file__)) + '/input')
lines = file.readlines()

s = ""
for i in lines:
    s += i + ' '

pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))")
res = pattern.findall(s)

disabled = False
acc = 0
for i in res:
    if i[3] != '':
        disabled = True
    elif i[2] != '':
        disabled = False
    else:
        d1 = i[0]
        d2 = i[1]
        r = int(d1) * int(d2)
        if not disabled:
            acc += r

print(acc)


